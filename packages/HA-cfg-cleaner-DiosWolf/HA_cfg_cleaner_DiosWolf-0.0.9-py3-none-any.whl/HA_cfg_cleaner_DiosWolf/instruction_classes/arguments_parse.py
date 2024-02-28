import sys
from typing import TypeVar, Type
from dacite import from_dict
from HA_cfg_cleaner_DiosWolf.data_classes_json.args_parse import Arguments


class ConsoleArguments:
    T = TypeVar("T")
    args: Arguments

    def __init__(self):
        self.__get_args(Arguments)

    def __get_args_dict(self):
        args_dict = {}
        for arg in sys.argv:
            if "instruction.json" in arg:
                args_dict["inst_path"] = arg

            if "config_HA.json" in arg:
                args_dict["cfg_ha_path"] = arg

        if "inst_path" not in args_dict.keys():
            # args_dict["inst_path"] = "instruction.json"
            raise Exception("Cant find instructions.json file")

        if "cfg_ha_path" not in args_dict.keys():
            args_dict["cfg_ha_path"] = "HA_cfg_cleaner_DiosWolf/configs_HA/config_HA.json"

        return args_dict

    def __get_args(self, data_class: Type[T]) -> T:
        args_dict = self.__get_args_dict()
        self.args = from_dict(data_class=data_class, data=args_dict)
        return self.args
