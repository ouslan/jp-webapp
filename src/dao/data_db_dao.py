from dotenv import load_dotenv
import pandas as pd
import os
import psycopg2
from sqlalchemy import create_engine

load_dotenv()


class DAO:
    def __init__(self):
        db_user = os.environ.get("POSTGRES_USER")
        db_password = os.environ.get("POSTGRES_PASSWORD")
        db_name = os.environ.get("POSTGRES_DB")
        db_host = os.environ.get("POSTGRES_HOST")
        db_port = os.environ.get("POSTGRES_PORT")
        self.conn2 = create_engine(
            f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )
        self.conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port,
        )
        with open("src/data/schema.sql", "r") as file:
            sql_query = file.read()
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        self.conn.commit()

    def insert_forms(
        self, data_path: str, dtypes: dict, table_name: str, debug: bool = False
    ):
        df = pd.read_csv(data_path)
        df["form_id"] = df.index.values + 1
        df = df.astype(dtypes)
        df.to_sql(
            name=table_name,
            con=self.conn2,
            if_exists="append",
            chunksize=5000,
            index=False,
        )
        os.remove(data_path)
        if debug:
            print(
                "\033[0;36mPROCESS: \033[0m" + f"Data inserted into {table_name} table"
            )
