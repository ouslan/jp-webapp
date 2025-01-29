from sqlalchemy import create_engine
from dotenv import load_dotenv
import polars as pl
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
        df: pl.DataFrame,
        table_name: str,
        table_id: int,
        debug: bool = False,
    ):
        df = df.with_columns(form_id=pl.lit(table_id))
        df.write_database(
            table_name=table_name,
            connection=self.conn2,
            if_table_exists="append",
        )
        df_id = pl.read_database(f'SELECT MAX(id) AS id FROM "{table_name}"', self.conn2)
        df_id = df_id.with_columns(form_id=pl.lit(table_id))
        df_id.write_database(
            table_name="Forms",
            connection=self.conn2,
            if_table_exists="append",
        )
        if debug:
             print("\033[0;36mINFO: \033[0m" + f"Inserted {table_name} to database")

