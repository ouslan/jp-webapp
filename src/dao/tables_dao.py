import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

class tables_DAO:
    def __init__(self):
        df_user = os.environ.get('POSTGRES_USER')
        df_password = os.environ.get('POSTGRES_PASSWORD')
        df_name = os.environ.get('POSTGRES_DB')
        connection_url = (f"dbname={df_name} " f"user={df_user} " f"password={df_password} " 
             f"host=localhost " 
             "port=5433")
        self.conn = psycopg2.connect(connection_url)

    def create_country_tables(self):
        cursor = self.conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS countries(
                    id serial primary key,
                    country_name varchar(60)
                );
                """
        cursor.execute(query,)
        self.conn.commit()

    def create_imp_exp_tables(self):
        cursor = self.conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS Import_Export(
            id serial primary key,
            date TIMESTAMPTZ NOT NULL,
            country_name varchar(60) NOT NULL,
            exports FLOAT NOT NULL,
            imports FLOAT NOT NULL,
            net_value FLOAT NOT NULL
            );
            """
        cursor.execute(query,)
        self.conn.commit()

    def create_hypertable(self):
        cursor = self.conn.commit()
        query = """select create_hypertable(
            'Import_Export',
            interval '1 month'
        )
        """
        cursor.execute(query,)
        self.conn.commit()

if __name__ == "__main__":
    dao = tables_DAO()
    dao.create_imp_exp_tables()