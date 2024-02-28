from dataclasses import dataclass
from typing import List


# TODO: for instructions file
@dataclass
class BasePath:
    path: str


@dataclass
class BaseIntegrationsIds:
    integrations_ids: list[str]


@dataclass
class DeleteObjects(BasePath):
    objects_names: list[str]


@dataclass
class DeleteInConfig(BaseIntegrationsIds):
    config_id: str


@dataclass
class DeleteScript(BasePath):
    scripts_ids: list[str]


@dataclass
class DeleteObjects(BasePath):
    objects_names: list[str]


@dataclass
class CleanFolders(BasePath):
    folders_names: list[str]


@dataclass
class CleanFiles(BasePath):
    files_names: list[str]


@dataclass
class ChangeFiles(BasePath):
    new_content: list


@dataclass
class FindInFiles:
    report_path: str
    text_to_find: list[str]


@dataclass
class Instructions:
    delete_in_config: List[DeleteInConfig]
    delete_integrations: BaseIntegrationsIds
    enable_integration: BaseIntegrationsIds
    disable_integration: BaseIntegrationsIds
    delete_objects: List[DeleteObjects]
    delete_script: List[DeleteScript]
    clean_folders: List[CleanFolders]
    clean_files: List[CleanFiles]
    change_files: List[ChangeFiles]
    find_in_all_files: FindInFiles

    # def get_keys(self):
    #     keys = []
    #     for key in fields(Instructions):
    #         keys.append(key.name)
    #     return keys
