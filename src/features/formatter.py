import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def process_file(file_path: str):
    df = pd.read_csv(file_path)
    
    # Initialize a list to store DataFrames
    dataframes = []
    
    for column in df.columns:
        if column == "Meses":
            continue
        
        # Create a temporary DataFrame
        tmp = df[["Meses", column]].copy()
        tmp = tmp.rename(columns={column: file_path.split("/")[-1][:-4]})
        tmp["year"] = column
        tmp = tmp[["year", "Meses", file_path.split("/")[-1][:-4]]]
        
        # Append the temporary DataFrame to the list
        dataframes.append(tmp)
    
    # Concatenate all DataFrames in the list
    if dataframes:
        clean_df = pd.concat(dataframes, axis=0)
    else:
        # If no dataframes were added, return an empty DataFrame with the desired columns
        clean_df = pd.DataFrame(columns=['year', 'Meses', file_path.split("/")[-1][:-4]])
        
    return clean_df
  
# df = process_file("data/external/INDICADORES ECÓNOMICOS/ENCUESTA DE ESTABLECIMIENTO/Actividades Financieras.csv")


for dirt in os.listdir("data/external/INDICADORES ECÓNOMICOS/"):
    for file in os.listdir(f"data/external/INDICADORES ECÓNOMICOS/{dirt}"):
        if file.endswith(".csv"):
            # print(f"Processing {file}")
            df = process_file(f"data/external/INDICADORES ECÓNOMICOS/{dirt}/{file}")
        try:
            master_df = master_df.merge(df, how="outer", on=["year", "Meses"])
        except NameError:
            master_df = df
 
master_df.columns = master_df.columns.str.strip().str.replace(",", "")
master_df.replace(" ","", regex=True, inplace=True)
                 
master_df.to_csv("data/external/indicadores_economicos.csv", index=False)