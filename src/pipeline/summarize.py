from src.config import ConfigManager
from transformers import AutoTokenizer
from transformers import pipeline


def summarize(text):
    config = ConfigManager().get_eval_config()
    tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_path)

    pipe = pipeline("summarization", model=config.model_path, tokenizer=tokenizer)

    return pipe(
        text, length_penalty = 0.8, num_beams = 8, max_length = 128
    )[0]["summary_text"]