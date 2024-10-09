from src.constants import CONFIG_PATH, PARAMS_PATH
from src.utils import create_dirs, read_yaml
from src.classes_config import DataConfig, TokenizationConfig, TrainerConfig, EvalConfig
from os.path import join


class ConfigManager:
    def __init__(self, config_path=CONFIG_PATH, params_path=PARAMS_PATH):
        self.params = read_yaml(params_path)
        self.config = read_yaml(config_path)

        self.artifacts = self.config.artifacts_folder_dir
        create_dirs([self.artifacts])

    def get_data_config(self):

        data_config = self.config.data

        return DataConfig(
            name=data_config.name,
            save_path=join(self.artifacts, data_config.folder)
        )

    def get_tokenization_config(self):
        config = self.config.tokenization
        direct = join(self.artifacts, config.folder)

        create_dirs([direct])

        return TokenizationConfig(
            direct=direct,
            model_name=config.model_name,
            data_path=self.get_data_config().save_path
        )

    def get_trainer_config(self):
        config = self.config.fine_tuning
        tokenization_config = self.config.tokenization
        params = self.params.TrainingArgs

        direct = join(self.artifacts, config.folder)

        create_dirs([direct])

        return TrainerConfig(
            config_path=direct,
            config_model_name=config.model_name,
            config_tokenizer_name=tokenization_config.model_name,
            config_tokenized_data_path=join(self.artifacts, tokenization_config.folder),
            params_epochs=params.epochs,
            params_warmup_steps=params.warmup_steps,
            params_batch_size=params.batch_size,
            params_weight_decay=params.weight_decay,
            params_logging_steps=params.logging_steps,
            params_evaluation_strategy=params.evaluation_strategy,
            params_eval_steps=params.eval_steps,
            params_save_steps=params.save_steps,
            params_gradient_accumulation_steps=params.gradient_accumulation_steps
        )

    def get_eval_config(self):
        direct = join(self.artifacts, self.config.evaluation.folder)
        create_dirs([direct])

        model_path = self.get_trainer_config().config_path+'/model'
        tokenizer_path = self.get_trainer_config().config_path+'/tokenizer'
        data_path = self.get_data_config().save_path

        return EvalConfig(
            folder_path=direct,
            model_path=model_path,
            tokenizer_path=tokenizer_path,
            data_path=data_path
        )