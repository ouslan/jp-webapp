from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import psycopg2
import os

load_dotenv()


class DAO:
    def __init__(self):
        db_user = os.environ.get("POSTGRES_USER")
        db_password = os.environ.get("POSTGRES_PASSWORD")
        db_name = os.environ.get("POSTGRES_DB")
        db_host = os.environ.get("POSTGRES_HOST")
        db_port = 5432
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
        self,
        data_path: str,
        dtypes: dict,
        table_name: str,
        table_id: int,
        debug: bool = False,
    ):
        df = pd.read_csv(data_path)
        df.columns = df.columns.str.strip()
        df["form_id"] = table_id
        print(df.columns)
        df = df.astype(dtypes)
        df.to_sql(
            name=table_name,
            con=self.conn2,
            if_exists="append",
            chunksize=5000,
            index=False,
        )
        df_id = pd.read_sql(f'SELECT MAX(id) AS id FROM "{table_name}"', self.conn2)
        df_id["form_id"] = table_id
        df_id.to_sql(
            name="Forms",
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
