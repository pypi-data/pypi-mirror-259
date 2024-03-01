import json
from typing import Dict, List, Tuple
from ..session import Session
from ..client import Client
from .compute_nodes import (
    ComputationNode,
    PythonComputeNode,
    RComputeNode,
    SqlComputeNode,
    SqliteComputeNode,
    S3SinkComputeNode,
    MatchingComputeNode,
    SyntheticDataComputeNode,
    PreviewComputeNode,
)
from .data_nodes import DataNode, RawDataNode, TableDataNode
from decentriq_dcr_compiler.schemas.data_science_data_room import (
    ScriptingComputationNode,
    SqlComputationNode,
    SqliteComputationNode,
    S3SinkComputationNode,
    MatchingComputationNode,
    SyntheticDataComputationNode,
    PreviewComputationNode,
    RawLeafNode,
    TableLeafNodeV2,
    DataScienceDataRoom,
    InteractiveDataScienceDataRoomV6,
    LeafNodeV2,
    ComputationNodeV6,
    ScriptingLanguage,
    Participant,
    DataOwnerPermission,
    AnalystPermission,
)


class ExistingDataScienceDcrBuilder:
    def __init__(self, dcr_id: str, client: Client, session: Session) -> None:
        self.dcr_id = dcr_id
        self.client = client
        self.session = session
        self.high_level = None
        self._retrieve_dcr()

    def _retrieve_dcr(self):
        existing_dcr = self.session.retrieve_data_room(self.dcr_id)
        self.high_level = json.loads(existing_dcr.highLevelRepresentation.decode())

    def get_nodes(self) -> Tuple[List[ComputationNode], List[DataNode]]:
        dcr = DataScienceDataRoom.model_validate(self.high_level).root
        try:
            interactive_dcr = InteractiveDataScienceDataRoomV6.model_validate(
                dcr.v6.root.interactive
            )
        except:
            raise Exception("Only interactive DCRs are supported")

        computation_nodes = []
        data_nodes = []
        participants = [
            Participant.model_validate(participant)
            for participant in interactive_dcr.initialConfiguration.participants
        ]
        (compute_node_permissions, data_node_permissions) = (
            self._get_node_permissions_dict(participants)
        )
        for node in interactive_dcr.initialConfiguration.nodes:
            id = node.id
            name = node.name
            root_node = node.kind.root
            node_fields = root_node.model_fields

            if "computation" in node_fields:
                assert id in compute_node_permissions
                parsed_node = ComputationNodeV6.model_validate(
                    node.kind.root.computation
                )
                computation_node = self._get_computation_node(
                    id, name, parsed_node, compute_node_permissions[id]
                )
                computation_nodes.append(computation_node)
            elif "leaf" in node_fields:
                assert id in data_node_permissions
                parsed_node = LeafNodeV2.model_validate(node.kind.root.leaf)
                data_node = self._get_data_node(
                    id, name, parsed_node, data_node_permissions[id]
                )
                data_nodes.append(data_node)
            else:
                raise Exception("Unknown node type")
        return (computation_nodes, data_nodes)

    def _get_computation_node(
        self,
        id: str,
        name: str,
        node: ComputationNodeV6,
        permissions: List[str],
    ) -> ComputationNode:
        root_node = node.kind.root
        node_fields = root_node.model_fields
        compute_node = None
        if "scripting" in node_fields:
            parsed_node = ScriptingComputationNode.model_validate(root_node.scripting)
            if parsed_node.scriptingLanguage == ScriptingLanguage.python:
                compute_node = PythonComputeNode.from_high_level(
                    id, name, parsed_node, permissions
                )
            elif parsed_node.scriptingLanguage == ScriptingLanguage.r:
                compute_node = RComputeNode.from_high_level(
                    id, name, parsed_node, permissions
                )
            else:
                raise Exception(
                    f"Unknown scripting language {parsed_node.scriptingLanguage}"
                )
        elif "sql" in node_fields:
            parsed_node = SqlComputationNode.model_validate(root_node.sql)
            compute_node = SqlComputeNode.from_high_level(
                id, name, parsed_node, permissions
            )
        elif "sqlite" in node_fields:
            parsed_node = SqliteComputationNode.model_validate(root_node.sqlite)
            compute_node = SqliteComputeNode.from_high_level(
                id, name, parsed_node, permissions
            )
        elif "s3Sink" in node_fields:
            parsed_node = S3SinkComputationNode.model_validate(root_node.s3Sink)
            compute_node = S3SinkComputeNode.from_high_level(
                id, name, parsed_node, permissions
            )
        elif "match" in node_fields:
            parsed_node = MatchingComputationNode.model_validate(root_node.match)
            compute_node = MatchingComputeNode.from_high_level(
                id, name, parsed_node, permissions
            )
        elif "syntheticData" in node_fields:
            parsed_node = SyntheticDataComputationNode.model_validate(
                root_node.syntheticData
            )
            compute_node = SyntheticDataComputeNode.from_high_level(
                id, name, parsed_node, permissions
            )
        elif "preview" in node_fields:
            parsed_node = PreviewComputationNode.model_validate(root_node.preview)
            compute_node = PreviewComputeNode.from_high_level(
                id, name, parsed_node, permissions
            )
        else:
            raise Exception("Unknown computation node type")
        compute_node.set_dcr_id(self.dcr_id)
        compute_node.set_session(self.session)
        compute_node.set_client(self.client)
        return compute_node

    def _get_data_node(
        self, id: str, name: str, node: LeafNodeV2, permissions: List[str]
    ) -> DataNode:
        is_required = node.isRequired
        root_node = node.kind.root
        node_fields = root_node.model_fields
        data_node = None
        if "raw" in node_fields:
            parsed_node = RawLeafNode.model_validate(root_node.raw)
            data_node = RawDataNode.from_high_level(
                id, name, parsed_node, is_required, permissions
            )
        elif "table" in node_fields:
            parsed_node = TableLeafNodeV2.model_validate(root_node.table)
            data_node = TableDataNode.from_high_level(
                id,
                name,
                parsed_node,
                is_required,
                permissions,
            )
        else:
            raise Exception("Unknown data node type")
        data_node.set_dcr_id(self.dcr_id)
        data_node.set_session(self.session)
        data_node.set_client(self.client)
        return data_node

    @staticmethod
    def _get_node_permissions_dict(
        participants: List[Participant],
    ) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
        node_data_permissions = {}
        node_compute_permissions = {}
        for participant in participants:
            user = participant.user
            for permission in participant.permissions:
                root_permission = permission.root
                permission_fields = root_permission.model_fields
                if "dataOwner" in permission_fields:
                    data_owner = DataOwnerPermission.model_validate(
                        root_permission.dataOwner
                    )
                    node_id = data_owner.nodeId
                    users = node_data_permissions.setdefault(data_owner.nodeId, [])
                    users.append(user)
                    node_data_permissions[node_id] = users
                elif "analyst" in permission_fields:
                    analyst = AnalystPermission.model_validate(root_permission.analyst)
                    node_id = analyst.nodeId
                    users = node_data_permissions.setdefault(node_id, [])
                    users.append(user)
                    node_compute_permissions[node_id] = users
        return (node_compute_permissions, node_data_permissions)
