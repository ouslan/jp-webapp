import pandas as pd


class DataProcessByDate:
  
  def __init__(self, parquet_path: str, saving_path: str, debug: bool = False):
    self.parquet_path = parquet_path
    self.saving_path = saving_path
    self.debug = debug
    self.df = pd.read_parquet(self.parquet_path)
    
    self.quarterly_df = self.to_quarterly(self.df)
    self.quarterly_df.to_parquet(f"{self.saving_path}Indicadores_Trimestrales.parquet")
    
    self.annual_df = self.to_annual(self.df)
    self.annual_df.to_parquet(f"{self.saving_path}Indicadores_Anuales.parquet")
    
  def to_quarterly(self, df):
    df["date"] = pd.to_datetime(df["date"])
    df2 = df.copy()
    
    df2["quarter"] = df2["date"].dt.to_period("Q")
    df2 = df2.groupby("quarter").agg("mean").round(2).reset_index()
    
    return df2


  def to_annual(self, df):
    df["date"] = pd.to_datetime(df["date"])
    df3 = df.copy()
    
    df3["year"] = df3["date"].dt.to_period("Y")
    df3 = df3.groupby("year").agg("mean").round(2).reset_index()

    return df3

