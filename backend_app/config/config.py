import yaml
from yaml.loader import SafeLoader
from pathlib import Path
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

current_directory = Path(__file__).parent

def read_params(path: Path):
    try:
        with open(path, 'r') as file:
            return yaml.load(file, Loader=SafeLoader)
        
    except yaml.YAMLError as e:
        logging.error(f'Invalid yaml file or corrupted yaml file: {e}')
        sys.exit()
    except Exception as e:
        logging.error(f'Error by reading yaml file: {e}')
        sys.exit()

params = read_params(current_directory / 'params.yaml')