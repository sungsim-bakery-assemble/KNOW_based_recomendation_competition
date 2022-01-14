from utils.models import load_model
from utils.utils import check_params, load_yaml
from utils.data import load_data, train_val_split

import os
import pickle as pkl
from sklearn.metrics import accuracy_score, f1_score
from argparse import ArgumentParser

if __name__ == "__main__":
    # Load configs
    parser = ArgumentParser()
    parser.add_argument("--config_path", type=str,  help=".yml Config file path" , required=True)
    args = parser.parse_args()
    configs = load_yaml(args.config_path)
    
    # Set basic params
    model_name = configs['model_name']
    
    # Train / val data split
    train_data, val_data =\
        train_val_split(load_data(configs['train_data_path']))
    
    y_train = train_data.pop('knowcode')
    X_train = train_data
    
    y_val = val_data.pop('knowcode')
    X_val = val_data

    # Load model backbone
    model = load_model(model_name, check_params(configs['hp'][model_name]))
    
    # fitting and save model
    if model_name in ['xgboost','lightgbm']:

        model.fit(X_train, y_train)
        
        real = y_val
        pred = model.predict(X_val)

        # logging at console
        print(f"{configs['exp_name']} is fitted....")
        print(f"\taccuracy : {accuracy_score(real, pred)}")
        print(f"\tf1-score : {f1_score(real, pred)}")

        with open(os.path.join(configs['model_save_dir'], configs['exp_name'], ".pkl"), 'wb') as f:
            pkl.dump(model, f)
        
