from src.components.tuning import Model
from src.config import ConfigManager
from src import logger


step = "Step 3: Fine tune the model on the tokenized data"


class tune:
    def main():
        global config
        config = ConfigManager().get_trainer_config()
        Model(config=config).fit()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>  Processing {step}...  <<<<<<<")
        tokenize.main()
        logger.info(f'<<<<<<<  Step 3 was completed successfully and the model was saved at "{config.direct}"...  >>>>>>>')

    except Exception as e:
        logger.exception(e)
        raise e