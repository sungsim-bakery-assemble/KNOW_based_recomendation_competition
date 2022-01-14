from sklearn.model_selection import train_test_split
import pandas as pd
from typing import Tuple

def load_data(data_path : str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(data_path, **kwargs)

def train_val_split(
    df : pd.DataFrame,
    train_size : float = 0.8,
    label : str= "knowcode",
    random_state : int = 42
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    
    train_df, val_df = train_test_split(
        df, 
        train_size=train_size, 
        random_state=random_state, 
        stratify=df[label]
    )

    return train_df, val_df
