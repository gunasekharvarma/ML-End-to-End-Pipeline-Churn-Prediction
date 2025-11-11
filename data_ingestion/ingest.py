import pandas as pd

def load_dataset(path):
    print("Loading dataset...")
    df = pd.read_csv(path)
    print("Dataset loaded")
    print(df.head())
    return df

if __name__ == "__main__":
    load_dataset("../data/Churn_Modelling.csv")
