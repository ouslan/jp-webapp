import pandas as pd

class DataProcess:

    def __init__(self, file_path: str):
        self.file_path = file_path


    def process_file(self, file_path: str):
        df = pd.read_csv(file_path)
        clean_df = pd.DataFrame(columns = ['Meses', file_path.split("/")[-1][:-4], "year"]) 
        for column in df.columns:
            if column == "Meses":
                continue
            tmp = df[["Meses", column]].copy()
            tmp = df.rename(columns={column:file_path.split("/")[-1][:-4]})
            tmp["year"] = column
            clean_df = pd.concat([clean_df, tmp], axis=0)
            clean_df.sort_values(by=["year", "Meses"])
        return clean_df

def process_data(self): 
    pass
