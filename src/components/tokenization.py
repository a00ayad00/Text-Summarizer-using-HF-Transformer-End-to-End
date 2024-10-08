from transformers import AutoTokenizer
from datasets import load_from_disk
from src.classes_config import TokenizationConfig
from datasets.utils.logging import disable_progress_bar


disable_progress_bar()


class Tokenization:
    def __init__(self, config: TokenizationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name)

    def to_ids(self, examples):
        inputs = self.tokenizer(examples['dialogue'], max_length=1024, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            targets = self.tokenizer(examples['summary'], max_length=128, truncation=True)

        return {
            'input_ids': inputs['input_ids'],
            'attention_`mask': inputs['attention_mask'],
            'labels': targets['input_ids']
        }

    def tokenize(self):
        data = load_from_disk(self.config.data_path)
        tokenized_data = data.map(self.to_ids, batched=True)
        tokenized_data.save_to_disk(self.config.direct)