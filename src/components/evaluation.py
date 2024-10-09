from datasets import load_from_disk
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import evaluate
import torch
import json
from src import logger
from tqdm import tqdm
from src.classes_config import EvalConfig


class Eval:
    def __init__(self, config: EvalConfig):
        self.config = config

    def generate_batch(self, list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size]

    def eval(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        test_data = load_from_disk(self.config.data_path, )['test']

        inp_batches = list(self.generate_batch(test_data['dialogue'], 16))
        tar_batches = list(self.generate_batch(test_data['summary'], 16))

        rouge_metric = evaluate.load('rouge')

        for inp_batch, tar_batch in tqdm(zip(inp_batches, tar_batches), total=len(inp_batches)):

            inputs = tokenizer(
                inp_batch, max_length=1024, padding='max_length', truncation=True, return_tensors="pt"
            )
            summaries = model.generate(
                input_ids=inputs["input_ids"].to(device),
                attention_mask=inputs["attention_mask"].to(device),
                length_penalty=0.8, num_beams=8, max_length=128
            )

            decoded_summaries = [
                tokenizer.decode(summary, skip_special_tokens=True, clean_up_tokenization_spaces=True)
                for summary in summaries
            ]

            rouge_metric.add_batch(predictions=decoded_summaries, references=tar_batch)

        metrics = rouge_metric.compute()

        with open(self.config.folder_path+'/eval.json', "w") as f:
            json.dump(metrics, f, indent=4)
            logger.info(f"Evaluation file saved at: {self.config.folder_path}")