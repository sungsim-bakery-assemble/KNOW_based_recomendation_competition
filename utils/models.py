from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from typing import Dict, Optional, Union

def load_model(
    model_name : str, 
    config : Dict,
) -> Union[XGBClassifier, LGBMClassifier] :
    """
        Load models backbone 
        
        Arguments
            - model_name : str, backbone model name , args = ( xgboost, lightgbm, torch )   
            - config : dict, Experiment condition config dictionary (Hyper parameters)
        
        Return
            - proper backbone instance
    """
    models = {
        "xgboost"   : XGBClassifier,
        "lightgbm"  : LGBMClassifier,
        "torch" : None, # Implementing...
    }
    model = models(**config)

    return model