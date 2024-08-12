import pandas as pd


class DataProcessByDate:
  
  def __init__(self, csv_path: str, saving_path: str, debug: bool = False):
    self.csv_path = csv_path
    self.saving_path = saving_path
    self.debug = debug
    self.df = pd.read_csv(self.csv_path)
    
    self.quarterly_df = self.to_quarterly(self.df)
    self.quarterly_df.to_csv(f"{self.saving_path}quarterly_master.csv")
    
    self.annual_df = self.to_annual(self.df)
    self.annual_df.to_csv(f"{self.saving_path}annual_master.csv")
    
  def to_quarterly(self, df):
    df["date"] = pd.to_datetime(df["date"])
    df2 = df.copy()
    
    df2["quarter"] = df2["date"].dt.to_period("Q")
    df2 = df2.groupby("quarter").agg("mean").round(2)
    
    return df2


  def to_annual(self, df):
    df["date"] = pd.to_datetime(df["date"])
    df3 = df.copy()
    
    df3["year"] = df3["date"].dt.to_period("Y")
    df3 = df3.groupby("year").agg("mean").round(2)

    return df3

