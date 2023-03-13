import yaml
from enum import Enum

with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

class FileConfig(Enum):
    filePath = config['filePath']
    dataSource = config['dataSource']
    dataSourceType = config['dataSourceType']