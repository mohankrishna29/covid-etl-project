import requests
import pandas as pd

def extract_data():
    url = "https://disease.sh/v3/covid-19/countries"
    reponse = requests.get(url)
    data = reponse.json()
    df = pd.json_normalize(data)
    df = df[["country", "cases", "deaths", "recovered", "casesPerOneMillion",
    "deathsPerOneMillion", "tests", "testsPerOneMillion", "population", "continent"]]
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())

