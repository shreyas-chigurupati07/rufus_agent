import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

project_name = 'rufusAgent'

list_of_files = [
    'Dockerfile',
    'LICENSE',
    'README.md',
    'requirements.txt',
    'setup.py',
    '.env',
    '.gitignore',
    'data/raw/.gitkeep',
    'data/processed/.gitkeep',
    'data/output.json',
    'research/exploration.ipynb',
    'research/web_scraping_tests.ipynb',
    'tests/__init__.py',
    'tests/test_scraper.py',
    'tests/test_api.py',
    'tests/test_utils.py',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/scraper.py',
    f'src/{project_name}/processor.py',
    f'src/{project_name}/api.py',
    f'src/{project_name}/utils.py',
    f'src/{project_name}/config.py',
    f'src/{project_name}/logger.py',
    f'src/{project_name}/models/__init__.py',
    'main.py',
    'template.py',
    'deployment/docker-compose.yml',
    'deployment/k8s/.gitkeep',
    'deployment/cloud_run.yaml',
    'deployment/aws_lambda.py',
    'deployment/heroku.yml'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created directory: {filedir} for the file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Created empty file: {filename} in the directory: {filedir}')
    else:
        logging.info(f'File: {filename} already exists in the directory: {filedir}')
