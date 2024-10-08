from src.pipeline.data_load import data
from src.pipeline.tokenize import tokenize
from src.pipeline.tune import tune


data.main()


tokenize.main()


tune.main()