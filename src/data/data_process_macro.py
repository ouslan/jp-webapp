import polars as pl
        
def process_file(file_path: str):
    df = pl.read_csv(file_path)
    
    df.columns = [col.strip().replace(',', "").replace('$', '').replace(" )", ")").replace("  ", " ").replace("( ", " (").replace('"', '').replace(' ', '') for col in df.columns]

    df = df.with_columns([
        pl.when(pl.col(col).str.contains('"') | pl.col(col).str.contains(' ') | pl.col(col).str.contains('()') )
        .then(pl.col(col).str.replace(',', '').str.replace(' ', '').replace("(", "").replace(")", ""))
        .otherwise(pl.col(col))
        .alias(col)
        for col in df.columns
    ])
    
    df.write_csv("data/raw/Series-historicas_COPY_TEST.csv")



def main() -> None:
  process_file("data/raw/Series-historicas-1950-2011.csv")
    
    
if __name__ == "__main__":
  main()
    