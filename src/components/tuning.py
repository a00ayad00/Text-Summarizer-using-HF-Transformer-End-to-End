from datasets import load_from_disk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
import torch
from src.classes_config import TrainerConfig


class Model:
    def __init__(self, config: TrainerConfig):
        self.config = config

    def fit(self):
        tokenized_data = load_from_disk(self.config.config_tokenized_data_path)
        tokenizer = AutoTokenizer.from_pretrained(self.config.config_tokenizer_name)

        device = 'cuda' if torch.cuda.is_available() else "cpu"
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.config_model_name).to(device)
        
        data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)
        
        args = TrainingArguments(
            output_dir=self.config.config_path,
            num_train_epochs=self.config.params_epochs,
            warmup_steps=self.config.params_warmup_steps,
            per_device_train_batch_size=self.config.params_batch_size,
            per_device_eval_batch_size=self.config.params_batch_size,
            weight_decay=self.config.params_weight_decay,
            logging_steps=self.config.params_logging_steps,
            evaluation_strategy=self.config.params_evaluation_strategy,
            eval_steps=self.config.params_eval_steps,
            save_steps=int(self.config.params_save_steps),
            gradient_accumulation_steps=self.config.params_gradient_accumulation_steps
        )


        model = Trainer(
            model=model, args=args,
            tokenizer=tokenizer, data_collator=data_collator,
            train_dataset=tokenized_data["train"], 
            eval_dataset=tokenized_data["validation"]
        )

        model.train()

        model.save_pretrained(join(self.config.config_path, 'model'))
        tokenizer.save_pretrained(join(self.config.config_path, 'tokenizer'))