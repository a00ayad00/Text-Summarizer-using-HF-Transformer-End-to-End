from dataclasses import dataclass


@dataclass
class DataConfig:
    name: str
    save_path: str


@dataclass
class TokenizationConfig:
    direct: str
    model_name: str
    data_path: str


@dataclass
class TrainerConfig:
    config_path: str
    config_model_name: str
    config_tokenizer_name: str
    config_tokenized_data_path: str
    params_epochs: int
    params_warmup_steps: int
    params_batch_size: int
    params_weight_decay: float
    params_logging_steps: int
    params_evaluation_strategy: str
    params_eval_steps: int
    params_save_steps: int
    params_gradient_accumulation_steps: int


@dataclass
class EvalConfig:
    folder_path: str
    model_path: str
    tokenizer_path: str
    data_path: str