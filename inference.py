import os
import pickle as pkl
from argparse import ArgumentParser

from utils.utils import load_yaml
from utils.data import load_data

def read_model(inference_model_path : str):
    
    if ".pkl" in inference_model_path:
        with open(inference_model_path, "rb") as f:
            model = pkl.load(f)

    return model


if __name__ == "__main__":
    # Load configs
    parser = ArgumentParser()
    parser.add_argument("--config_path", type=str,  help=".yml Config file path" , required=True)
    args = parser.parse_args()
    configs = load_yaml(args.config_path)

    data  = load_data(configs['train_data_path'])
    model = read_model(configs['inference_model_path'])

    if configs['model_name'] in ['xgboost', 'lightgbm']:
        data['knowcode'] = model.predict(data)

    results = data[['idx', 'knowcode']]
    results.to_csv(os.path.join(configs['results'], configs['exp_name'], ".csv"), index=False)