from src.constants import CONFIG_PATH, PARAMS_PATH
from src.utils import create_dirs, read_yaml
from src.classes_config import DataConfig
import os


class ConfigManager:
    def __init__(self, config_path=CONFIG_PATH, params_path=PARAMS_PATH):
        self.params = read_yaml(config_path)
        self.config = read_yaml(config_path)

        self.artifacts = self.config.artifacts_folder_dir
        create_dirs([self.artifacts])

    def get_data_config(self):

        data_config = self.config.data

        return DataConfig(
            name=data_config.name,
            save_path=os.path.join(self.artifacts, data_config.folder)
        )