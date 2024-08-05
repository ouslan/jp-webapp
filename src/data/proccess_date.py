import pandas as pd

def trimestral(df, option):
  df["date"] = pd.to_datetime(df["date"])
  df2 = df[["date", option]].copy()
  df2["quarter"] = df2["date"].dt.to_period("Q")
  df2 = df2.groupby("quarter").agg({option: ["mean"]})
  df2.columns = [f"{option}_mean"]
  return df2

def anual(df, option):
  df["date"] = pd.to_datetime(df["date"])
  df2 = df[["date", option]].copy()
  df2["year"] = df2["date"].dt.to_period("Y")
  df2 = df2.groupby("year").agg({option: ["mean"]})
  df2.columns = [f"{option}_mean"]
  return df2


if __name__ == "__main__":
  df = pd.read_csv("data/processed/master.csv")
  print(anual(df, "Movimiento de pasajeros en el aeropuerto José Aponte de la Torre (NRR)"))