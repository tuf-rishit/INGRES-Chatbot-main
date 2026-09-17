import pandas as pd
import os

def get_groundwater_data():
    # Path of this file
    base = os.path.dirname(os.path.abspath(__file__))
    
    # TXT file inside the database folder
    filepath = os.path.join(base, "mp_gw_data.txt")
    
    return pd.read_csv(filepath)