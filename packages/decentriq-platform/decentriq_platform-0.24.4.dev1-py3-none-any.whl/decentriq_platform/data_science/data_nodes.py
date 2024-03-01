from enum import Enum
import io
import json
from typing import Dict, Optional, List, BinaryIO
import zipfile
from .high_level_node import DataNode
from dataclasses import dataclass
from ..client import Client
from ..storage import Key
from ..helpers import get_latest_enclave_specs_as_dictionary
from ..session import Session
from decentriq_dcr_compiler.schemas.data_science_data_room import (
    RawLeafNode,
    TableLeafNodeV2,
)


class RawDataNode(DataNode):
    def __init__(
        self,
        name: str,
        data_owners: List[str],
        is_required: bool,
        id: Optional[str] = None,
    ) -> None:
        super().__init__(name, is_required, data_owners, id)
        self.data_owners = data_owners

    def get_high_level_representation(self) -> Dict[str, str]:
        raw_node = {
            "id": self.id,
            "name": self.name,
            "kind": {"leaf": {"isRequired": self.is_required, "kind": {"raw": {}}}},
        }
        return raw_node

    def from_high_level(
        id: str,
        name: str,
        _node: RawLeafNode,
        is_required: bool,
        data_owners: List[str],
    ):
        return RawDataNode(
            name=name, id=id, is_required=is_required, data_owners=data_owners
        )


class ColumnDataType(str, Enum):
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"


@dataclass
class ColumnDataFormat:
    dataType: ColumnDataType
    isNullable: bool


class FormatType(str, Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    EMAIL = "EMAIL"
    DATE_ISO8601 = "DATE_ISO8601"
    PHONE_NUMBER_E164 = "PHONE_NUMBER_E164"
    HASH_SHA256_HEX = "HASH_SHA256_HEX"

    @staticmethod
    def from_column_data_type(fmt: ColumnDataType) -> str:
        if fmt == ColumnDataType.INTEGER:
            return FormatType.INTEGER.value
        elif fmt == ColumnDataType.FLOAT:
            return FormatType.FLOAT.value
        elif fmt == ColumnDataType.STRING:
            return FormatType.STRING.value
        else:
            raise Exception(
                f"Unable to convert column data type {fmt.value} to a format type"
            )


class HashingAlgorithm(str, Enum):
    SHA256_HEX = "SHA256_HEX"


class NumericRangeRule:
    greaterThan: Optional[float] = None
    greaterThanEquals: Optional[float] = None
    lessThan: Optional[float] = None
    lessThanEquals: Optional[float] = None


@dataclass
class Column:
    dataFormat: ColumnDataFormat
    name: str
    hashWith: Optional[HashingAlgorithm] = None
    inRange: Optional[NumericRangeRule] = None


class TableDataNode(DataNode):
    def __init__(
        self,
        name: str,
        columns: List[Column],
        data_owners: List[str],
        is_required: bool,
        id: Optional[str] = None,
    ) -> None:
        super().__init__(name, is_required, data_owners, id)
        self.columns = columns

    def get_high_level_representation(self) -> Dict[str, str]:
        column_entries = []
        for column in self.columns:
            validation = {
                "name": column.name,
                "formatType": FormatType.from_column_data_type(
                    column.dataFormat.dataType
                ),
                "allowNull": column.dataFormat.isNullable,
            }
            if column.hashWith:
                validation["hashWith"] = column.hashWith.value
            if column.inRange:
                validation["inRange"] = column.inRange.value
            column_entries.append(
                {
                    "name": column.name,
                    "dataFormat": {
                        "isNullable": column.dataFormat.isNullable,
                        "dataType": column.dataFormat.dataType.value,
                    },
                    "validation": validation,
                }
            )

        table_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "leaf": {
                    "isRequired": self.is_required,
                    "kind": {
                        "table": {
                            "columns": column_entries,
                            "validationNode": {
                                "staticContentSpecificationId": "decentriq.driver",
                                "pythonSpecificationId": "decentriq.python-ml-worker-32-64",
                                "validation": {},
                            },
                        }
                    },
                }
            },
        }
        return table_node

    # This data node needs to override the `super` implementation because
    # the leaf ID requires the "_leaf" suffix.
    def upload_and_publish_data(self, data: BinaryIO, key: Key, file_name: str):
        if not self.dcr_id:
            raise Exception("Data node is not part of a data room")

        manifest_hash = self.client.upload_dataset(data, key, file_name)
        self.session.publish_dataset(
            self.dcr_id, manifest_hash, leaf_id=f"{self.id}_leaf", key=key
        )

    def get_name(self) -> str:
        return self.name

    def from_high_level(
        id: str,
        name: str,
        node: TableLeafNodeV2,
        is_required: bool,
        data_owners: List[str],
    ):
        node_dict = json.loads(node.model_dump_json())
        columns = [
            Column(
                dataFormat=ColumnDataFormat(**column["dataFormat"]),
                name=column["name"],
                hashWith=column["validation"]["hashWith"],
                inRange=column["validation"]["inRange"],
            )
            for column in node_dict["columns"]
        ]
        return TableDataNode(
            name=name,
            columns=columns,
            data_owners=data_owners,
            id=id,
            is_required=is_required,
        )

    def get_validation_report(self) -> Dict[str, str]:
        validation_node_id = f"{self.id}_validation_report"
        result = self.session.run_computation_and_get_results(
            self.dcr_id, validation_node_id, interval=1
        )

        validation_report = {}
        zip = zipfile.ZipFile(io.BytesIO(result), "r")
        if "validation-report.json" in zip.namelist():
            validation_report = json.loads(zip.read("validation-report.json").decode())
        return validation_report
