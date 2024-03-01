import base64
from enum import Enum
from typing import Dict, List, Optional
from typing_extensions import Self
import uuid
from ..client import Client
from ..attestation import SPECIFICATIONS, EnclaveSpecifications
from decentriq_dcr_compiler import compiler
from decentriq_dcr_compiler.schemas.data_science_data_room import DataScienceDataRoom
from decentriq_dcr_compiler.schemas.data_science_commit import DataScienceCommit
from ..session import (
    LATEST_WORKER_PROTOCOL_VERSION,
    Session,
)
from ..proto.length_delimited import parse_length_delimited, serialize_length_delimited
from ..proto import DataRoom, CreateDcrKind, ConfigurationCommit
from .compute_nodes import ComputationNode
from .data_nodes import DataNode
from .commits import ComputationCommit
from .existing_builder import ExistingDataScienceDcrBuilder


class DataScienceDcrType(str, Enum):
    STATIC = "STATIC"
    INTERACTIVE = "INTERACTIVE"


class ParticipantPermission(Enum):
    DATA_OWNER = 1
    ANALYST = 2


class DataScienceDcrBuilder:
    """
    A helper class to build a Data Science DCR.
    """

    def __init__(
        self,
        client: Client,
        enclave_specs: Optional[Dict[str, EnclaveSpecifications]] = None,
    ) -> None:
        """
        Initialise the Data Science DCR builder.

        If enclave specifications are not provided the latest specifications will be used.
        """
        self.client = client
        self.enclave_specs = enclave_specs
        self.name = None
        self.description = ""
        self.owner = None
        self.data_nodes = []
        self.compute_nodes = []
        self.dcr_id = None
        self.enable_allow_empty_files_invalidation = False
        self.enable_development = False
        self.enable_safe_python_worker_stack_trace = False
        self.enable_server_side_wasm_validation = False
        self.enable_test_datasets = False
        self.enable_airlock = False
        self.nodes = None
        self.participants = None
        self.dcr_type = DataScienceDcrType.INTERACTIVE
        self.commits = None
        self.enable_auto_merge_feature = False
        self.dcr_secret_id_base_64 = None
        self.compile_context = None

    def from_existing(self, dcr_id: str):
        self.dcr_id = dcr_id
        data_room_descriptions = self.client.get_data_room_descriptions()
        existing_data_room_description = [
            description
            for description in data_room_descriptions
            if description["id"] == self.dcr_id
        ]
        if len(existing_data_room_description) != 1:
            raise Exception(
                f"Unable to retrieve data room description for data room with ID {self.dcr_id}"
            )

        specs = EnclaveSpecifications(self.enclave_specs)
        session = self.client.create_session_from_data_room_description(
            existing_data_room_description[0], specs
        )
        existing_dcr_builder = ExistingDataScienceDcrBuilder(
            self.dcr_id, self.client, session
        )
        (self.compute_nodes, self.data_nodes) = existing_dcr_builder.get_nodes()

    def get_compute_nodes(self) -> List[ComputationNode]:
        return self.compute_nodes

    def get_data_nodes(self) -> List[DataNode]:
        return self.data_nodes

    def with_name(self, name: str) -> Self:
        """
        Set the name of the Data Science DCR.

        **Parameters**:
        - `name`: Name to be used for the Data Science DCR.
        """
        self.name = name
        return self

    def with_description(self, description: str) -> Self:
        """
        Set the description of the Data Science DCR.

        **Parameters**:
        - `description`: Description of the Data Science DCR.
        """
        self.description = description
        return self

    def with_participants(self, participants: List[str]) -> Self:
        self.participants = participants
        return self

    def with_auto_merge(self) -> Self:
        self.enable_auto_merge_feature = True
        return self

    def with_owner(self, owner: str) -> Self:
        self.owner = owner
        return self

    def with_development_mode(self) -> Self:
        self.enable_development = True
        return self

    def with_airlock(self) -> Self:
        self.enable_airlock = True

    def add_data_node(self, node: DataNode) -> str:
        self.data_nodes.append(node)
        return node.get_id()

    def add_compute_node(self, node: ComputationNode) -> str:
        self.compute_nodes.append(node)
        return node.get_id()

    def build_and_publish(self):
        if not self.owner:
            raise Exception("The data room owner must be specified")

        permissions = self._get_participant_permissions()
        all_nodes = self.compute_nodes + self.data_nodes
        nodes = [node.get_high_level_representation() for node in all_nodes]
        ds_dcr = {
            "v6": {
                "interactive": {
                    "commits": [],
                    "enableAutomergeFeature": self.enable_auto_merge_feature,
                    "initialConfiguration": {
                        "description": self.description,
                        "enableAirlock": self.enable_airlock,
                        "enableAllowEmptyFilesInValidation": self.enable_allow_empty_files_invalidation,
                        "enableDevelopment": self.enable_development,
                        "enablePostWorker": False,
                        "enableSafePythonWorkerStacktrace": self.enable_safe_python_worker_stack_trace,
                        "enableServersideWasmValidation": self.enable_server_side_wasm_validation,
                        "enableSqliteWorker": False,
                        "enableTestDatasets": self.enable_test_datasets,
                        "enclaveRootCertificatePem": self.client.decentriq_ca_root_certificate.decode(),
                        "enclaveSpecifications": self._get_hl_specs(),
                        "id": self._generate_id(),
                        "nodes": nodes,
                        "participants": permissions,
                        "title": self.name,
                    },
                }
            }
        }

        # print(ds_dcr)

        data_room = DataScienceDataRoom.model_validate(ds_dcr)
        compiled_data_room = compiler.compile_data_science_data_room(data_room)
        self.compile_context = compiled_data_room.compile_context

        session = self._get_session()
        low_level_data_room = DataRoom()
        parse_length_delimited(compiled_data_room.data_room, low_level_data_room)
        self.dcr_id = session.publish_data_room(
            low_level_data_room,
            kind=CreateDcrKind.DATASCIENCE,
            high_level_representation=compiled_data_room.datascience_data_room_encoded,
        )

        for node in all_nodes:
            # Associate the node with this DCR.
            node.set_dcr_id(self.dcr_id)
            # Set the session for future node operations.
            node.set_session(session)
            # Set the client for future node operations.
            node.set_client(self.client)

        return self.dcr_id

    def add_computation_to_existing_dcr(
        self,
        node: ComputationNode,
    ) -> ComputationCommit:
        if not self.dcr_id:
            raise Exception("Data room must be built before it can be modified.")
        elif not self.enable_development:
            raise Exception("Data room does not have development mode enabled")
        elif not self.compile_context:
            raise Exception("Data room compile context not initialised")

        # Associate the node with the DCR.
        node.set_dcr_id(self.dcr_id)

        # TODO need to get the correct session
        session = self._get_session()
        (_current_config, history_pin) = (
            session.retrieve_current_data_room_configuration(self.dcr_id)
        )
        computation_commit = ComputationCommit(
            history_pin=history_pin,
            node=node,
        )
        computation_commit.set_dcr_id(self.dcr_id)
        computation_commit.set_session(self._get_session())
        computation_commit.set_client(self.client)
        hl = {"v6": computation_commit.get_high_level_representation()}
        ds_commit = DataScienceCommit.parse_obj(hl)
        compiled_commit = compiler.compile_data_science_commit(
            ds_commit, self.compile_context
        )
        # Update the context.
        self.compile_context = compiled_commit.compile_context

        cfg_commit = ConfigurationCommit()
        parse_length_delimited(compiled_commit.commit, cfg_commit)
        commit_id = session.publish_data_room_configuration_commit(cfg_commit)
        computation_commit.set_commit_id(commit_id)
        return computation_commit

    def _get_session(self) -> Session:
        enclave_specs = (
            SPECIFICATIONS if self.enclave_specs is None else self.enclave_specs
        )
        auth, _ = self.client.create_auth_using_decentriq_pki(enclave_specs)
        session = self.client.create_session(auth, enclave_specs)
        return session

    def _get_hl_specs(self):
        enclave_specs = (
            SPECIFICATIONS if self.enclave_specs is None else self.enclave_specs
        )
        specs = [
            {
                "attestationProtoBase64": base64.b64encode(
                    serialize_length_delimited(spec["proto"])
                ).decode(),
                "id": name,
                "workerProtocol": LATEST_WORKER_PROTOCOL_VERSION,
            }
            for name, spec in enclave_specs.items()
        ]
        return specs

    def _get_participant_permissions(self):
        if not self.participants:
            raise Exception("Data room does not have any participants")

        participants = []
        for participant in self.participants:
            hl_permissions = []
            for node in self.data_nodes:
                if node.is_data_owner(participant):
                    hl_permissions.append({"dataOwner": {"nodeId": node.get_id()}})
            for node in self.compute_nodes:
                if node.is_analyst(participant):
                    hl_permissions.append({"analyst": {"nodeId": node.get_id()}})
            if self.owner == participant:
                hl_permissions.append({"manager": {}})
            participants.append(
                {
                    "user": participant,
                    "permissions": hl_permissions,
                }
            )
        return participants

    @staticmethod
    def _generate_id():
        return str(uuid.uuid4())
