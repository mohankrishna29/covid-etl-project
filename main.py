from src.extract import extract_data
from src.transform import transform
from src.load import load_data

if __name__ == "__main__":
    df = extract_data()
    df = transform(df)
    load_data(df)
