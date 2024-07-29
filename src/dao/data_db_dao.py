from dotenv import load_dotenv
import os
import psycopg2
from sqlalchemy import create_engine

load_dotenv()


class DAO:
    def __init__(self):
        super().__init__()
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

    def insert_forms(self):
        pass
