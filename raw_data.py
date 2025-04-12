import pandas as pd
import os

def read_data():
    if not os.path.exists("raw_data.csv"):
        print("⚠️ No raw_data.csv file found. Please enter data first.")
        return []
    df = pd.read_csv("raw_data.csv")
    return df['Value'].tolist()