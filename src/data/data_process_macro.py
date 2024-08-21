import polars as pl


class DataProcessHistoricalSeries:

    def __init__(self, folder_path_1: str, folder_path_2: str, saving_path: str, debug: bool = False):
        self.folder_path_1 = folder_path_1
        self.folder_path_2 = folder_path_2
        self.saving_path = saving_path
        self.debug = debug

        self.df1 = self.process_data1(self.folder_path_1)
        self.df1.write_parquet(f"{self.saving_path}series-historicas-1950-2011_processed.parquet")   
        
        self.df2 = self.process_data2(self.folder_path_2)
        self.df2.write_parquet(f"{self.saving_path}series-historicas-2001-2023_processed.parquet")  
    
    
    def process_data1(self, folder_path: str):
        df1 = pl.read_parquet(folder_path)

        df1.columns = [col.strip().replace(',', "").replace('$', '').replace(" )", ")").replace("  ", " ").replace("    ", " ").replace("( ", " (").replace('"', '').upper() for col in df1.columns]

        df1 = df1.with_columns([
            pl.when(pl.col(col).str.contains("'") | pl.col(col).str.contains(",", literal=True) | pl.col(col).str.contains(' ') | pl.col(col).str.contains("(", literal=True) | pl.col(col).str.contains(")", literal=True) | pl.col(col).str.contains('n/d') | pl.col(col).str.contains('no disponible'))
              .then(pl.col(col).str.replace(',', '').str.replace("'", "").str.replace("(", "-", literal=True).str.replace(")", "", literal=True).replace("n/d", None).replace("no disponible", None).str.strip_chars().cast(pl.Float64))
              .otherwise(pl.col(col))
              .alias(col)
            for col in df1.columns
        ])

        return df1

    def process_data2(self, folder_path: str):
        df2 = self.process_data1(folder_path)

        df2 = df2.with_columns([
            (pl.col("PERIODO = AÑO FISCAL")
            .str.replace_all("'", "")
            .cast(pl.Float64)
            + 2000
            ).alias("PERIODO = AÑO FISCAL") 
        ])

        return df2

