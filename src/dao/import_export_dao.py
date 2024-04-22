import psycopg2
import os
import sqlalchemy
from dotenv import load_dotenv
load_dotenv()

class import_export_dao:
    def __init__(self):
        df_user = os.environ.get('POSTGRES_USER')
        df_password = os.environ.get('POSTGRES_PASSWORD')
        df_name = os.environ.get('POSTGRES_DB')
        connection_url = (f"dbname={df_name} " f"user={df_user} " f"password={df_password} " 
             f"host=localhost " 
             "port=5433")
        self.conn = psycopg2.connect(connection_url)

    def insert_transaction(self, date, country_name,exports,imports,net_value):
        cursor = self.conn.cursor()
        query = """insert into Import_Export(
        data,
        country_name,
        exports,
        imports,
        net_value) values (%s,%s,%s,%s,%s) return id;"""
        cursor.execute(query,(date, country_name,exports,imports,net_value,))
        imp_exp_id = cursor.fetchone()[0]
        self.conn.commit()
        return imp_exp_id
    

