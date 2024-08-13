import polars as pl


class DataProcessHistoricalSeries:
    
    def __init__(self, folder_path: str, saving_path: str, debug: bool = False):
        self.folder_path = folder_path
        self.saving_path = saving_path
        self.debug = debug
        self.df = self.process_data(self.folder_path)
        self.df.write_csv(f"{self.saving_path}Series-Historicas-1950-2011_processes.csv")   
         
    def process_data(self, folder_path: str):
        df = pl.read_csv(folder_path)
        
        df.columns = [col.strip().replace(',', "").replace('$', '').replace(" )", ")").replace("  ", " ").replace("( ", " (").replace('"', '').upper() for col in df.columns]

        df = df.with_columns([
            pl.when(pl.col(col).str.contains(' ') | pl.col(col).str.contains('()') | pl.col(col).str.contains('n/d') | pl.col(col).str.contains('no disponible'))
            .then(pl.col(col).str.replace(',', '').str.replace(' ', '').replace("(", "").replace(")", "").replace("n/d", None).replace("no disponible", None))
            .otherwise(pl.col(col))
            .alias(col)
            for col in df.columns
        ])
        
        return df
    