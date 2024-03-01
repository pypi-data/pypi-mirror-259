from abc import ABC, abstractmethod
from typing import Dict, BinaryIO, List, Optional
import uuid
from ..session import Session
from ..client import Client
from ..storage import Key
from ..types import JobId

__all__ = ["HighLevelNode"]


class HighLevelNode(ABC):
    def __init__(self, name: str, id=Optional[str]) -> None:
        super().__init__()
        self.id = str(uuid.uuid4()) if not id else id
        self.name = name
        self.dcr_id = None
        self.client = None
        self.session = None

    @abstractmethod
    def get_high_level_representation(self) -> Dict[str, str]:
        pass

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def set_dcr_id(self, dcr_id: str):
        self.dcr_id = dcr_id

    def get_dcr_id(self) -> Optional[str]:
        return self.dcr_id

    def set_client(self, client: Client):
        self.client = client

    def set_session(self, session: Session):
        self.session = session


class ComputationNode(HighLevelNode, ABC):
    def __init__(self, name: str, analysts: List[str], id=Optional[str]) -> None:
        super().__init__(name, id)
        self.analysts = analysts
        self.job_id = None

    def run_computation(self):
        if not self.session:
            raise Exception(
                f"Unable to run computation. Node {self.id} does not have an associated session"
            )
        self.job_id = self.session.run_computation(self.dcr_id, self.get_computation_id())

    def get_results(
        self,
        interval: Optional[int] = 5,
        timeout: Optional[int] = None,
    ) -> Optional[bytes]:
        if not self.job_id:
            raise Exception("A computation must be run before results can be retrieved")
        return self.session.get_computation_result(
            self.job_id, interval=interval, timeout=timeout
        )

    def run_computation_and_get_results(self):
        if not self.session:
            raise Exception(
                f"Unable to run computation. Node {self.id} does not have an associated session"
            )
        return self.session.run_computation_and_get_results(
            self.dcr_id, self.get_computation_id(), interval=1
        )

    @abstractmethod
    def get_computation_id(self) -> str:
        pass

    def is_analyst(self, user_email: str) -> bool:
        return user_email in self.analysts

    def get_analysts(self) -> List[str]:
        return self.analysts


class DataNode(HighLevelNode, ABC):
    def __init__(
        self, name: str, is_required: bool, data_owners: List[str], id=Optional[str]
    ) -> None:
        super().__init__(name, id)
        self.is_required = is_required
        self.data_owners = data_owners

    def upload_and_publish_data(self, data: BinaryIO, key: Key, file_name: str):
        if not self.dcr_id:
            raise Exception("Data node is not part of a data room")

        manifest_hash = self.client.upload_dataset(data, key, file_name)
        self.session.publish_dataset(
            self.dcr_id, manifest_hash, leaf_id=self.id, key=key
        )

    def is_data_owner(self, user_email: str) -> bool:
        return user_email in self.data_owners
