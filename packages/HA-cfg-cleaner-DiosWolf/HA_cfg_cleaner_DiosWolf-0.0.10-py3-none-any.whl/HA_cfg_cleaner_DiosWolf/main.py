from HA_cfg_cleaner_DiosWolf.instruction_classes.arguments_parse import ConsoleArguments
from HA_cfg_cleaner_DiosWolf.instruction_classes.fileIO_cls import FileIO
from HA_cfg_cleaner_DiosWolf.data_classes_json.file_config import ConfigurationFile
from HA_cfg_cleaner_DiosWolf.data_classes_json.instructions import Instructions
from HA_cfg_cleaner_DiosWolf.instruction_classes.instruction_executor import InstructionsExecute


class StartScript:
    def __init__(self):
        self.cls_args = ConsoleArguments()
        self.file_io = FileIO()
        self.all_instructions = self.file_io.json_read(
            self.cls_args.args.inst_path, Instructions)

        self.all_configs = self.file_io.json_read(
            self.cls_args.args.cfg_ha_path, ConfigurationFile)

        self.instruction_executor = InstructionsExecute(
            self.all_instructions, self.file_io, self.all_configs)

        self.instruction_executor.start()


def start_script():
    try:
        StartScript()
        input("Script finished. Press Enter to exit\n")
    except Exception as exp:
        print(exp)
        input("Error! Press Enter to exit\n")


if __name__ == "__main__":
    # try:
        start = StartScript()
        input("Script finished. Press Enter to exit\n")
    # except Exception as exp:
    #     print(exp)
