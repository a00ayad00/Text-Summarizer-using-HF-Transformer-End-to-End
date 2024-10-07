from src.components.data import Data
from src.config import ConfigManager
from src import logger


step = "Step 1: Load the data from the Hugging Face Hub"


class data:
    def main():
        config = ConfigManager().get_data_config()
        Data(config).download()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>  Processing {step}...  <<<<<<<")
        data.main()
        logger.info("<<<<<<<  Step 1 was completed successfully...  >>>>>>>")

    except Exception as e:
        logger.exception(e)
        raise e