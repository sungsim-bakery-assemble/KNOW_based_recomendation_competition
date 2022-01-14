import yaml
from typing import Dict

def load_yaml(config_path : str) -> Dict:
    """
        load config yml file
    """
    with open(config_path) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    return config


def check_params(params):
    return {key : val for key,val in params.items() if val}