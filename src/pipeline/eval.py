from src.components.evaluation import Eval
from src.config import ConfigManager
from src import logger


step = "Step 4: Evaluate the model on the test data"


class eval:
    def main():
        global config
        config = ConfigManager().get_eval_config()
        Eval(config).eval()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>  Processing {step}...  <<<<<<<")
        eval.main()
        logger.info(f'<<<<<<<  Step 4 was completed successfully and the file was saved at "{config.folder_path}"  >>>>>>>')

    except Exception as e:
        logger.exception(e)
        raise e