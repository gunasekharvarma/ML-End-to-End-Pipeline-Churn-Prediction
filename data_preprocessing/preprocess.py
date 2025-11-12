from data_ingestion.ingest import load_dataset


def preprocess(df):
    print('Date Preprocessing')
    print('Basic Dataset Info')
    print(df.info())
    print(df.head())

if __name__ == '__main__':
    df = load_dataset('../data/Churn_Modelling.csv')
    preprocess(df)