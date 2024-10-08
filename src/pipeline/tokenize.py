from src.components.tokenization import Tokenization
from src.config import ConfigManager
from src import logger


step = "Step 2: Tokenize the data"


class tokenize:
    def main():
        global config
        config = ConfigManager().get_tokenization_config()
        Tokenization(config).tokenize()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>  Processing {step}...  <<<<<<<")
        tokenize.main()
        logger.info(f'<<<<<<<  Step 2 was completed successfully and the tokenized data was saved at "{config.direct}"...  >>>>>>>')

    except Exception as e:
        logger.exception(e)
        raise e