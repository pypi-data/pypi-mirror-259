import os

from HA_cfg_cleaner_DiosWolf.instruction_classes.fileIO_cls import FileIO


class FindInAllFiles:
    def __init__(self):
        self.path = [
            # r"C:\Users\wolkm\OneDrive\Робочий стіл\file_checker\save_folder\config",
            "./config",
            "./addon_configs",
            "./addons",
            "./backup",
            "./media",
            "./share",
            "./ssl",
        ]
        self.report_io = FileIO()

    def __get_catalogue(self) -> dict[str, list]:
        catalogue_dict = {}
        for scn_path in self.path:
            files = os.walk(scn_path)
            for path, _, files in files:
                catalogue_dict[path] = files
        return catalogue_dict

    def __find_file(
        self, file_lines: list[bytes], file_path: str, text_to_find: list[str]
    ) -> dict[str, dict]:
        i = 0
        find_dict = {}
        for line in file_lines:
            i += 1
            for text in text_to_find:

                if text.encode(encoding="UTF-8") in line:
                    if text not in find_dict:
                        find_dict[text] = {}
                    elif file_path not in find_dict[text]:
                        find_dict[text][file_path] = []
                        find_dict[text][file_path].append(i)
                    else:
                        find_dict[text][file_path].append(i)
        return find_dict

    def start_find(self, text_to_find: list[str]) -> dict[str, dict]:
        catalogue = self.__get_catalogue()
        find_dict = {}
        for main_folder, files_dict in catalogue.items():

            for file in files_dict:
                file_path = main_folder + "/" + file
                file_lines = self.report_io.read_byte_lines(file_path)
                find_dict = find_dict | self.__find_file(
                    file_lines, file_path, text_to_find
                )
        find_dict = dict(filter(lambda x: x[1], find_dict.items()))
        return find_dict

    # def get_json_file(self, file: dict[str, str]):
    #     self.report_io.json_write("./find_report.json", file)
