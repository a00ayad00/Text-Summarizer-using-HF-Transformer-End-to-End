import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


paths_to_create = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components",
    "src/utils.py",
    "src/config.py",
    "src/pipeline",
    "src/classes_config.py",
    "config.yaml",
    "dvc.yml",
    "params.yaml",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "app.py",
    "main.py",
    "notebooks/trials.ipynb",
]


for path in paths_to_create:
    path = Path(path)
    direct, filename = os.path.split(path)

    if direct:
        os.makedirs(direct, exist_ok=True)
        logging.info(f'The directory "{direct}" was created successfully...')

    if not os.path.exists(path):
        with open(path, 'w'):
            logging.info(f'The file "{filename}" was created successfully at "{direct}"...')
    else:
        logging.info(f'The file "{filename}" already exists at "{direct}"')