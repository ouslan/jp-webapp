from src.data.data_process import DataProcess
from src.data.proccess_date import DataProcessByDate
from src.data.data_process_macro import DataProcessHistoricalSeries

def main() -> None:
    DataProcess("data/external/INDICADORES ECÓNOMICOS/", "data/processed/")
    
    DataProcessByDate("data/processed/master.csv", "data/processed/")
    
    DataProcessHistoricalSeries("data/raw/Series-historicas-1950-2011.csv", "data/processed/")

if __name__ == "__main__":
    main()
