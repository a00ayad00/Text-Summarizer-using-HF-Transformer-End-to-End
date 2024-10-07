from src import logger
from src.utils import get_size
from src.classes_config import DataConfig
from datasets import load_dataset
from datasets.utils.logging import disable_progress_bar


disable_progress_bar()


class Data:
    def __init__(self, data_config: DataConfig):
        self.config = data_config

    def download(self):
        name = self.config.name
        path = self.config.save_path

        data = load_dataset(self.config.name)
        data.save_to_disk(self.config.save_path)
        logger.info(f'The data "{name}" loaded successfully and saved at "{path}" with size {get_size(path)} MB')