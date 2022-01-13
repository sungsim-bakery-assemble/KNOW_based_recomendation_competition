from utils.models import load_model
from utils.utils import load_yaml

from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--config_path", type=str,  help=".yml Config file path" , required=True)
    args = parser.parse_args()
    
    configs = load_yaml(args.config_path)
    