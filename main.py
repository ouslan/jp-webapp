from src.data.data_process import DataProcess
from src.data.proccess_date import DataProcessByDate
from src.data.data_process_macro import DataProcessHistoricalSeries
from src.data.idb import DataProcessIDB

def main() -> None:
    DataProcess("data/IndicadoresEconomicos/", "data/processed/")
    DataProcessByDate("data/processed/Indicadores_Economicos.parquet", "data/processed/")
    DataProcessHistoricalSeries("data/raw/Series-Historicas-1950-2011.parquet", "data/raw/Series-Historicas-2001-2023.parquet", "data/processed/")
    DataProcessIDB()
    
if __name__ == "__main__":
    main()
