from dataclasses import dataclass, asdict
from enum import Enum
import json
from typing import Dict, List, Optional
from .high_level_node import ComputationNode
from .script import Script, ScriptingLanguage
from .data_nodes import ColumnDataFormat
from decentriq_dcr_compiler.schemas.data_science_data_room import (
    ScriptingComputationNode,
    SqlComputationNode,
    SqliteComputationNode,
    S3SinkComputationNode,
    MatchingComputationNode,
    SyntheticDataComputationNode,
    PreviewComputationNode,
)


@dataclass
class ScriptingNodeConfig:
    main_script: Script
    dependencies: Optional[List[str]] = None
    additional_scripts: Optional[List[Script]] = None
    enable_logs_on_error: Optional[bool] = False
    enable_logs_on_success: Optional[bool] = False
    output: Optional[str] = "/output"

    @staticmethod
    def from_dict(dictionary: Dict[str, str]):
        scripting_language = (
            ScriptingLanguage.python
            if dictionary["scriptingLanguage"] == "python"
            else ScriptingLanguage.r
        )
        main_script = Script(
            name=dictionary["mainScript"]["name"],
            content=dictionary["mainScript"]["content"],
            language=scripting_language,
        )
        return ScriptingNodeConfig(
            main_script=main_script,
            dependencies=dictionary["dependencies"],
            additional_scripts=dictionary["additionalScripts"],
            enable_logs_on_error=dictionary["enableLogsOnError"],
            enable_logs_on_success=dictionary["enableLogsOnSuccess"],
            output=dictionary["output"],
        )


PythonConfig = ScriptingNodeConfig


class PythonComputeNode(ComputationNode):
    def __init__(
        self,
        name: str,
        config: PythonConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        language = config.main_script.get_scripting_language()
        if language != ScriptingLanguage.python:
            raise Exception(
                f"Python compute node cannot support the {language} scripting language"
            )
        super().__init__(name, analysts, id)
        self.cfg = config
        self.scripting_specification_id = "decentriq.python-ml-worker-32-64"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        dependencies = [] if not self.cfg.dependencies else self.cfg.dependencies
        additional_scripts = (
            [] if not self.cfg.additional_scripts else self.cfg.additional_scripts
        )
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "scripting": {
                            "additionalScripts": additional_scripts,
                            "dependencies": dependencies,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "mainScript": {
                                "name": self.cfg.main_script.get_name(),
                                "content": self.cfg.main_script.get_content(),
                            },
                            "output": self.cfg.output,
                            "scriptingLanguage": self.cfg.main_script.get_scripting_language(),
                            "scriptingSpecificationId": self.scripting_specification_id,
                            "staticContentSpecificationId": self.static_content_specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_id(self) -> str:
        return self.id

    def get_computation_id(self) -> str:
        # ID to use when running a computation
        return f"{self.id}_container"

    def from_high_level(
        id: str, name: str, node: ScriptingComputationNode, analysts: List[str]
    ):
        config = PythonConfig.from_dict(json.loads(node.model_dump_json()))
        return PythonComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


RConfig = ScriptingNodeConfig


class RComputeNode(ComputationNode):
    def __init__(
        self,
        name: str,
        config: RConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        language = config.main_script.get_scripting_language()
        if language != ScriptingLanguage.r:
            raise Exception(
                f"R compute node cannot support the {language} scripting language"
            )
        super().__init__(name, analysts, id)
        self.cfg = config
        self.scripting_specification_id = "decentriq.r-latex-worker-32-32"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        dependencies = [] if not self.cfg.dependencies else self.cfg.dependencies
        additional_scripts = (
            [] if not self.cfg.additional_scripts else self.cfg.additional_scripts
        )
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "scripting": {
                            "additionalScripts": additional_scripts,
                            "dependencies": dependencies,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "mainScript": {
                                "name": self.cfg.main_script.get_name(),
                                "content": self.cfg.main_script.get_content(),
                            },
                            "output": self.cfg.output,
                            "scriptingLanguage": self.cfg.main_script.get_scripting_language(),
                            "scriptingSpecificationId": self.scripting_specification_id,
                            "staticContentSpecificationId": self.static_content_specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_id(self) -> str:
        return self.id

    def get_computation_id(self) -> str:
        # ID to use when running a computation
        return f"{self.id}_container"

    def from_high_level(
        id: str, name: str, node: ScriptingComputationNode, analysts: List[str]
    ):
        node_json = json.loads(node.model_dump_json())
        config = RConfig.from_dict(node_json)
        return RComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


@dataclass
class TableMapping:
    nodeId: str
    tableName: str


@dataclass
class SqlNodeConfig:
    sql_statement: str
    dependencies: Optional[List[TableMapping]] = None
    minimum_rows_count: Optional[int] = None

    @staticmethod
    def from_dict(dictionary: Dict[str, str]):
        minimum_rows_count = (
            None
            if not dictionary["privacyFilter"]
            else dictionary["privacyFilter"]["minimumRowsCount"]
        )
        return SqlNodeConfig(
            dependencies=dictionary["dependencies"],
            sql_statement=dictionary["statement"],
            minimum_rows_count=minimum_rows_count,
        )


class SqlComputeNode(ComputationNode):
    def __init__(
        self,
        name: str,
        config: SqlNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.sql-worker"

    def get_high_level_representation(self) -> Dict[str, str]:
        dependencies = []
        if self.cfg.dependencies:
            for dependency in self.cfg.dependencies:
                dependencies.append(
                    {
                        "nodeId": dependency.nodeId,
                        "tableName": dependency.tableName,
                    }
                )

        sql = {
            "dependencies": dependencies,
            "specificationId": self.specification_id,
            "statement": self.cfg.sql_statement,
        }
        if self.cfg.minimum_rows_count:
            sql["privacyFilter"]["minimumRowsCount"] = self.cfg.minimum_rows_count

        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "sql": sql,
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        return self.id

    def from_high_level(
        id: str, name: str, node: SqlComputationNode, analysts: List[str]
    ):
        node_json = json.loads(node.model_dump_json())
        config = SqlNodeConfig.from_dict(node_json)
        return SqlComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


@dataclass
class SqliteNodeConfig:
    sqlite_statement: str
    dependencies: Optional[List[TableMapping]] = None
    enable_logs_on_error: Optional[bool] = False
    enable_logs_on_success: Optional[bool] = False

    @staticmethod
    def from_dict(dictionary: Dict[str, str]):
        return SqliteNodeConfig(
            dependencies=dictionary["dependencies"],
            sqlite_statement=dictionary["statement"],
            enable_logs_on_error=dictionary["enableLogsOnError"],
            enable_logs_on_success=dictionary["enableLogsOnSuccess"],
        )


class SqliteComputeNode(ComputationNode):
    def __init__(
        self,
        name: str,
        config: SqliteNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.python-ml-worker-32-64"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        dependencies = []
        if self.cfg.dependencies:
            for dependency in self.cfg.dependencies:
                dependencies.append(
                    {
                        "nodeId": dependency.nodeId,
                        "tableName": dependency.tableName,
                    }
                )
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "sqlite": {
                            "dependencies": dependencies,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "sqliteSpecificationId": self.specification_id,
                            "statement": self.cfg.sqlite_statement,
                            "staticContentSpecificationId": self.static_content_specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        return f"{self.id}_container"

    def from_high_level(
        id: str, name: str, node: SqliteComputationNode, analysts: List[str]
    ):
        node_json = json.loads(node.model_dump_json())
        config = SqliteNodeConfig.from_dict(node_json)
        return SqliteComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


class MaskType(str, Enum):
    GENERIC_STRING = "genericString"
    GENERIC_NUMBER = "genericNumber"
    NAME = "name"
    ADDRESS = "address"
    POSTCODE = "postcode"
    PHONE_NUMBER = "phoneNumber"
    SOCIAL_SECURITY_NUMBER = "socialSecurityNumber"
    EMAIL = "email"
    DATE = "date"
    TIMESTAMP = "timestamp"
    IBAN = "iban"


@dataclass
class SyntheticNodeColumn:
    dataFormat: ColumnDataFormat
    index: int
    maskType: MaskType
    shouldMaskColumn: bool
    name: Optional[Optional[str]] = None


@dataclass
class SyntheticNodeConfig:
    columns: List[SyntheticNodeColumn]
    dependency: str
    epsilon: float
    output_original_data_statistics: Optional[bool] = False
    enable_logs_on_error: Optional[bool] = False
    enable_logs_on_success: Optional[bool] = False

    @staticmethod
    def from_dict(dictionary: Dict[str, str]):
        return SqliteNodeConfig(
            columns=dictionary["columns"],
            dependency=dictionary["dependency"],
            epsilon=dictionary["epsilon"],
            output_original_data_statistics=dictionary["outputOriginalDataStatistics"],
            enable_logs_on_error=dictionary["enableLogsOnError"],
            enable_logs_on_success=dictionary["enableLogsOnSuccess"],
        )


class SyntheticDataComputeNode(ComputationNode):
    def __init__(
        self,
        name: str,
        config: SyntheticNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.python-synth-data-worker-32-64"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        columns = [asdict(column) for column in self.cfg.columns]
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "syntheticData": {
                            "columns": columns,
                            "dependency": self.cfg.dependency,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "epsilon": self.cfg.epsilon,
                            "outputOriginalDataStatistics": self.cfg.output_original_data_statistics,
                            "staticContentSpecificationId": self.static_content_specification_id,
                            "synthSpecificationId": self.specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        return f"{self.id}_container"

    def from_high_level(
        id: str, name: str, node: SyntheticDataComputationNode, analysts: List[str]
    ):
        node_json = json.loads(node.model_dump_json())
        config = SqliteNodeConfig.from_dict(node_json)
        return SyntheticDataComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


class S3Provider(str, Enum):
    AWS = "Aws"
    GCS = "Gcs"


@dataclass
class S3SinkNodeConfig:
    credentials_dependency_id: str
    endpoint: str
    region: str
    upload_dependency_id: str
    s3_provider: Optional[S3Provider] = S3Provider.AWS

    @staticmethod
    def from_dict(dictionary: Dict[str, str]):
        return SqliteNodeConfig(
            credentials_dependency_id=dictionary["credentialsDependencyId"],
            endpoint=dictionary["endpoint"],
            region=dictionary["region"],
            upload_dependency_id=dictionary["uploadDependencyId"],
            s3_provider=dictionary["s3Provider"],
        )


class S3SinkComputeNode(ComputationNode):
    def __init__(
        self,
        name: str,
        config: S3SinkNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.s3-sink-worker"

    def get_high_level_representation(self) -> Dict[str, str]:
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "s3Sink": {
                            "credentialsDependencyId": self.cfg.credentials_dependency_id,
                            "endpoint": self.cfg.endpoint,
                            "region": self.cfg.region,
                            "s3Provider": self.cfg.s3_provider.value,
                            "specificationId": self.specification_id,
                            "uploadDependencyId": self.cfg.upload_dependency_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        return self.id

    def from_high_level(
        id: str, name: str, node: S3SinkComputationNode, analysts: List[str]
    ):
        node_json = json.loads(node.model_dump_json())
        config = S3SinkNodeConfig.from_dict(node_json)
        return S3SinkComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


@dataclass
class MatchingComputeNodeConfig:
    query: List[str]
    round: int
    epsilon: int
    sensitivity: int
    dependency_paths: List[str]


@dataclass
class MatchingNodeConfig:
    config: MatchingComputeNodeConfig
    dependencies: List[str]
    enable_logs_on_error: Optional[bool] = False
    enable_logs_on_success: Optional[bool] = False
    output: Optional[str] = "/output"

    @staticmethod
    def from_dict(dictionary: Dict[str, str]):
        config = json.loads(dictionary["config"])
        return MatchingNodeConfig(
            config=MatchingComputeNodeConfig(**config),
            dependencies=dictionary["dependencies"],
            enable_logs_on_error=dictionary["enableLogsOnError"],
            enable_logs_on_success=dictionary["enableLogsOnSuccess"],
            output=dictionary["output"],
        )


class MatchingComputeNode(ComputationNode):
    def __init__(
        self,
        name: str,
        config: MatchingNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.python-ml-worker-32-64"
        self.static_content_specification_id = "decentriq.driver"

    def get_high_level_representation(self) -> Dict[str, str]:
        dependencies = [] if not self.cfg.dependencies else self.cfg.dependencies
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "match": {
                            "config": json.dumps(asdict(self.cfg.config)),
                            "dependencies": dependencies,
                            "enableLogsOnError": self.cfg.enable_logs_on_error,
                            "enableLogsOnSuccess": self.cfg.enable_logs_on_success,
                            "output": self.cfg.output,
                            "specificationId": self.specification_id,
                            "staticContentSpecificationId": self.static_content_specification_id,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        return f"{self.id}_match_filter_node"

    def from_high_level(
        id: str, name: str, node: MatchingComputationNode, analysts: List[str]
    ):
        node_json = json.loads(node.model_dump_json())
        config = MatchingNodeConfig.from_dict(node_json)
        return MatchingComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )


@dataclass
class PreviewNodeConfig:
    dependency: str
    quota_bytes: Optional[int] = 0

    @staticmethod
    def from_dict(dictionary: Dict[str, str]):
        return PreviewNodeConfig(
            dependency=dictionary["dependency"],
            quota_bytes=dictionary["quotaBytes"],
        )


class PreviewComputeNode(ComputationNode):
    def __init__(
        self,
        name: str,
        config: PreviewNodeConfig,
        analysts: List[str],
        id: Optional[str] = None,
    ) -> None:
        super().__init__(name, analysts, id)
        self.cfg = config
        self.specification_id = "decentriq.python-ml-worker-32-64"

    def get_high_level_representation(self) -> Dict[str, str]:
        computation_node = {
            "id": self.id,
            "name": self.name,
            "kind": {
                "computation": {
                    "kind": {
                        "preview": {
                            "dependency": self.cfg.dependency,
                            "quotaBytes": self.cfg.quota_bytes,
                        }
                    }
                },
            },
        }
        return computation_node

    def get_computation_id(self) -> str:
        return self.id

    def from_high_level(
        id: str, name: str, node: PreviewComputationNode, analysts: List[str]
    ):
        node_json = json.loads(node.model_dump_json())
        config = PreviewNodeConfig.from_dict(node_json)
        return PreviewComputeNode(
            name=name,
            id=id,
            config=config,
            analysts=analysts,
        )
