from ast import parse
from json import load
from models import load_model
from argparse import ArgumentParser
from utils import load_yaml


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--config_path", type=str,  help=".yml Config file path" , required=True)
    args = parser.parse_args()
    
    configs = load_yaml(args.config_path)    
    