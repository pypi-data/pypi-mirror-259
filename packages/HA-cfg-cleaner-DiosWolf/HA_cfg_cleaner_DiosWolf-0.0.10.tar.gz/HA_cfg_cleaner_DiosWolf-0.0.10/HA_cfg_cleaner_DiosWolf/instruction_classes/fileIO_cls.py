from ruamel.yaml import YAML
import json
from typing import Type, TypeVar
from dacite import from_dict
from HA_cfg_cleaner_DiosWolf.instruction_classes.parse_cls import ParseFileInfo


class FileIO:
    T = TypeVar("T")

    def __init__(self):
        self.yaml = YAML()
        self.yaml.preserve_quotes = True
        self.json = json
        self.parser = ParseFileInfo()

    def yaml_read(self, path: str, data_class: Type[T] = False) -> T | dict[any]:
        with open(path, "r", encoding="utf-8") as reader:
            data = self.yaml.load(reader)

            if data_class:
                return from_dict(data_class=data_class, data=data)
            else:
                return data

    def yaml_write(self, path: str, file: any):
        with open(path, "w", encoding="utf8") as writer:
            self.yaml.dump(file, writer)
            writer.close()

    def json_read(self, path: str, data_class: Type[T] = False) -> T | dict[any]:
        with open(path, "rb") as reader:
            data = self.json.load(reader)

            if data_class:
                return from_dict(data_class=data_class, data=data)
            else:
                return data

    def json_write(self, path: str, file: any):
        with open(path, "w", encoding="utf8") as writer:
            self.json.dump(file, writer, indent=2, sort_keys=False, ensure_ascii=False)
            writer.close()

    def read_with_type(self, path: str, file_type: str = None):
        if file_type is None:
            file_type = self.parser.get_type(path)

        if file_type == ".yaml":
            return self.yaml_read(path)
        elif file_type == ".json":
            return self.json_read(path)

    def write_with_type(self, path: str, file: any, file_type: str = None):
        if file_type is None:
            file_type = self.parser.get_type(path)

        if file_type == ".yaml":
            self.yaml_write(path, file)
        elif file_type == ".json":
            self.json_write(path, file)

    def read_byte_lines(self, path: str) -> list[bytes]:
        with open(path, "rb") as file:
            return file.readlines()
