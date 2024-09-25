from src.data.data_process import DataProcess
from src.data.proccess_date import DataProcessByDate
from src.data.data_process_macro import DataProcessHistoricalSeries
from src.data.idb import DataProcessIDB

def main() -> None:
    DataProcess("data/indicadores_economicos/", "data/processed/")
    DataProcessByDate("data/processed/indicadores_economicos.parquet", "data/processed/")
    DataProcessHistoricalSeries("data/raw/series-historicas-1950-2011.parquet", "data/raw/series-historicas-2001-2023.parquet", "data/processed/")
    DataProcessIDB()

if __name__ == "__main__":
    main()
