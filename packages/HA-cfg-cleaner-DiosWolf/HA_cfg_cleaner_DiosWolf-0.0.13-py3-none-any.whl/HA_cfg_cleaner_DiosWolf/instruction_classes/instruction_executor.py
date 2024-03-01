from HA_cfg_cleaner_DiosWolf.data_classes_json.file_config import ConfigurationFile
from HA_cfg_cleaner_DiosWolf.data_classes_json.instructions import Instructions
from HA_cfg_cleaner_DiosWolf.instruction_classes.fileIO_cls import FileIO
from HA_cfg_cleaner_DiosWolf.instruction_classes.file_folder_editor_cls import FileFoldersEditor
from HA_cfg_cleaner_DiosWolf.instruction_classes.find_in_files_cls import FindInAllFiles
from HA_cfg_cleaner_DiosWolf.instruction_classes.integrations_cls import IntegrationsEditor
from HA_cfg_cleaner_DiosWolf.instruction_classes.script_editor_cls import ScriptsEditor


class InstructionsExecute:
    def __init__(
        self,
        all_instructions: Instructions,
        file_io: FileIO,
        all_configs: ConfigurationFile,
    ):
        self.all_instructions = all_instructions
        self.all_configs = all_configs
        self.file_io = file_io

    def start(self):
        self.del_in_cfg()
        self.del_integrations()
        self.enable_integrations()
        self.disable_integrations()
        self.del_automations()
        self.change_files()
        self.del_script()
        self.del_objects()
        self.clean_folders()
        self.clean_files()
        self.searching_in_files()

    def del_in_cfg(self):
        pass

    def del_integrations(self):
        ids_list = self.all_instructions.delete_integrations.integrations_ids
        for configuration in self.all_configs.configurations:
            full_cfg = self.file_io.read_with_type(
                configuration.path + configuration.filename, configuration.type_cfg
            )
            integration_editor = IntegrationsEditor(configuration, full_cfg)

            try:
                new_cgf = integration_editor.delete_integration(ids_list)
                self.file_io.write_with_type(
                    configuration.path + configuration.filename,
                    new_cgf,
                    configuration.type_cfg,
                )
            except Exception as exp:
                print(exp)

    def enable_integrations(self):
        ids_list = self.all_instructions.enable_integration.integrations_ids

        for configuration in self.all_configs.configurations:
            full_cfg = self.file_io.read_with_type(
                configuration.path + configuration.filename, configuration.type_cfg
            )
            integration_editor = IntegrationsEditor(configuration, full_cfg)
            new_cgf = integration_editor.disable_enable_integration(
                ids_list, configuration.on_integration
            )
            self.file_io.write_with_type(
                configuration.path + configuration.filename,
                new_cgf,
                configuration.type_cfg,
            )

    def disable_integrations(self):
        ids_list = self.all_instructions.disable_integration.integrations_ids

        for configuration in self.all_configs.configurations:
            full_cfg = self.file_io.read_with_type(
                configuration.path + configuration.filename, configuration.type_cfg
            )
            integration_editor = IntegrationsEditor(configuration, full_cfg)

            new_cgf = integration_editor.disable_enable_integration(
                ids_list, configuration.off_integration
            )
            self.file_io.write_with_type(
                configuration.path + configuration.filename,
                new_cgf,
                configuration.type_cfg,
            )

    def del_automations(self):
        ids_list = self.all_instructions.delete_automations.integrations_ids

        for configuration in self.all_configs.automations_cfg:

            full_cfg = self.file_io.read_with_type(
                configuration.path + configuration.filename, configuration.type_cfg
            )
            integration_editor = IntegrationsEditor(configuration, full_cfg)

            try:
                new_cgf = integration_editor.delete_automation(ids_list)
                self.file_io.write_with_type(
                    configuration.path + configuration.filename,
                    new_cgf,
                    configuration.type_cfg,
                )
            except Exception as exp:
                print(exp)

    def del_script(self):
        for instruction in self.all_instructions.delete_script:

            full_cfg = self.file_io.read_with_type(instruction.path)
            script_editor = ScriptsEditor(full_cfg)

            for script_id in instruction.scripts_ids:
                try:
                    script_editor.delete_scripts(script_id)
                except Exception as exp:
                    print(exp)

            self.file_io.write_with_type(instruction.path, script_editor.edit_file)

    def del_objects(self):
        fl_fld_editor = FileFoldersEditor()
        for delete_object in self.all_instructions.delete_objects:
            for object_name in delete_object.objects_names:
                path = delete_object.path + "/" + object_name
                try:
                    fl_fld_editor.delete_objects(path)
                except Exception as exp:
                    print(exp)

    def clean_folders(self):
        fl_fld_editor = FileFoldersEditor()
        for delete_object in self.all_instructions.clean_folders:
            for object_name in delete_object.folders_names:
                path = delete_object.path + "/" + object_name
                try:
                    fl_fld_editor.clean_folders(path)
                except Exception as exp:
                    print(exp)

    def clean_files(self):
        fl_fld_editor = FileFoldersEditor()
        for delete_object in self.all_instructions.clean_files:
            for object_name in delete_object.files_names:
                path = delete_object.path + "/" + object_name
                try:
                    fl_fld_editor.clean_files(path)
                except Exception as exp:
                    print(exp)

    def change_files(self):
        for file_info in self.all_instructions.change_files:
            orig_file = self.file_io.read_with_type(file_info.path)
            file_editor = ScriptsEditor(orig_file)
            for new_part in file_info.new_content:
                file_editor.change_file(new_part)
            self.file_io.write_with_type(file_info.path, file_editor.edit_file)

    def searching_in_files(self):
        searcher = FindInAllFiles()
        find_dict = searcher.start_find(
            self.all_instructions.find_in_all_files.text_to_find
        )
        self.file_io.json_write(self.all_instructions.find_in_all_files.report_path, find_dict)
