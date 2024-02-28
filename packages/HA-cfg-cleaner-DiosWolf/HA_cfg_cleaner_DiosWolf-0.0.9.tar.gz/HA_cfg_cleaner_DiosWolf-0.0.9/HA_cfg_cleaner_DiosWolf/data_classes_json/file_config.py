# TODO: for file configurations
from dataclasses import dataclass
from typing import List


@dataclass
class Configuration:
    config_id: str
    filename: str
    first_key: str | None
    second_key: str | None
    id_key: str
    identifiers_key: str
    type_cfg: str
    path: str
    on_off_field: str
    on_integration: None | str
    off_integration: str


@dataclass
class ConfigurationFile:
    configurations: List[Configuration]
