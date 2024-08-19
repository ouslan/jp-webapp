import pandas as pd
import os

def to_parquet_file(file_path: str, saving_path: str):
    df = pd.read_csv(file_path)
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    df.to_parquet(os.path.join(saving_path, f"{file_name}.parquet"))

if __name__ == "__main__":
    to_parquet_file("data/external/ForecastAnual.csv", "data/external/")
    to_parquet_file("data/external/ForecastTrimestral.csv", "data/external/")
    
    for dir_name in os.listdir("data/external/INDICADORES ECÓNOMICOS"):
        dir_path = os.path.join("data/external/INDICADORES ECÓNOMICOS", dir_name)
        if os.path.isdir(dir_path):
            for file in os.listdir(dir_path):
                if file.endswith(".csv"):
                    file_path = os.path.join(dir_path, file)
                    to_parquet_file(file_path, dir_path)
                    
