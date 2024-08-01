import polars as pl
import os

class DataProcess:

    def __init__(self, folder_path: str, saving_path: str, debug: bool = False):
        self.folder_path = folder_path
        self.saving_path = saving_path
        self.debug = debug
        self.df = self.process_data(self.folder_path)
        self.df.write_csv(f"{self.saving_path}master.csv")

    def process_file(self, file_path: str):
        df = pl.read_csv(file_path)
        column_name = file_path.split("/")[-1][:-4]
        empty_df = [
            pl.Series("month", [], dtype=pl.Int64),
            pl.Series("year", [], dtype=pl.Int64),
            pl.Series(column_name, [], dtype=pl.Float64)
        ]
        clean_df = pl.DataFrame(empty_df)
        for column in df.columns:
            if column == "Meses":
                continue
            column_name = file_path.split("/")[-1][:-4]
            # Create a temporary DataFrame
            tmp = df
            tmp = tmp.rename({column:column_name})
            tmp = tmp.with_columns(
            pl.when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "enero").then(1)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "febrero").then(2)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "marzo").then(3)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "abril").then(4)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "mayo").then(5)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "junio").then(6)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "julio").then(7)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "agosto").then(8)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "septiembre").then(9)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "octubre").then(10)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "noviembre").then(11)
              .when(pl.col("Meses").str.strip_chars().str.to_lowercase() == "diciembre").then(12)
              .alias("month")           
                )
            tmp = tmp.with_columns(
                pl.col(column_name).str.replace_all("$", "", literal=True).str.replace_all(",", "").str.strip_chars().alias(column_name)
            )
            tmp = tmp.with_columns(
                pl.when(pl.col(column_name)  == "n/d").then(None)
                .when(pl.col(column_name)  == "**").then(None)
                .when(pl.col(column_name)  == "-").then(None)
                .when(pl.col(column_name)  == "no disponible").then(None)
                .otherwise(pl.col(column_name)).alias(column_name)
            )
            tmp = tmp.select(
                            pl.col("month").cast(pl.Int64).alias("month"),
                            pl.lit(int(column)).cast(pl.Int64).alias("year"),
                            pl.col(column_name).cast(pl.Float64).alias(column_name)
            )
            
            # Append the temporary DataFrame to the list
            clean_df = pl.concat([clean_df, tmp], how="vertical")
        
        
        return clean_df

    def process_data(self, folder_path: str): 
        for dirt in os.listdir(folder_path):
            for file in os.listdir(f"{folder_path}{dirt}"):
                if file.endswith(".csv"):
                    df = self.process_file(f"{folder_path}{dirt}/{file}")
                try:
                    master_df = master_df.join(df, on=["year", "month"], how="outer_coalesce")
                except NameError:
                    master_df = df
        return master_df
