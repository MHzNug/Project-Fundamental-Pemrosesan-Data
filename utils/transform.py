import pandas as pd
import numpy as np
from datetime import datetime
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
pd.set_option('mode.chained_assignment', None)  # default='warn'

def transform_data(products):
    # This function takes a list of product dictionaries and transforms it into a DataFrame.
    df = pd.DataFrame(products)
    
    df = df[df['title'].str.lower() != 'unknown product']
    
    df['price'] = df['price'].str.replace(r'[^\d.]', '', regex=True)
    df['price'] = df['price'].str.replace('.', '')
    df['price'] = df['price'].replace('', np.nan)
    df['price'] = df['price'].astype(float)
    df['price'].dropna(inplace=True)
    df['price'] = df['price'] * 16000
    
    df['rating'] = df['rating'].replace(r'[^0-9.]', '', regex=True)
    df['rating'] = df['rating'].replace('', np.nan)
    df['rating'] = df['rating'].astype(float)
    df['rating'].dropna(inplace=True)
    
    df['color'] = df['color'].str.replace(r'[\D]', '', regex=True)
    df['color'] = df['color'].replace('', np.nan)
    df['color'] = df['color'].astype(int)
    df['color'].dropna(inplace=True)
    
    df['size'] = df['size'].replace(r'Size:\s*', '', regex=True)
    df['gender'] = df['gender'].replace(r'Gender:\s*', '', regex=True)
    
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    
    return df