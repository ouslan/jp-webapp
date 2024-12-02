from dotenv import load_dotenv
import os

load_dotenv()

# Get the Database credentials
def get_db_credentials():
    USER = str(os.environ.get("POSTGRES_USER")).strip()
    HOST = str(os.getenv("POSTGRES_HOST")).strip()
    DATABASE = str(os.environ.get("POSTGRES_DB")).strip()
    SECRET_KEY = str(os.getenv("SECRET_KEY")).strip()

    if not all([HOST, USER, DATABASE, SECRET_KEY]):
        raise ValueError("Database credentials not set")
    if os.environ.get("DEV") == "True":
        HOST = "localhost"
        PASSWORD = str(os.getenv("POSTGRES_PASSWORD")).strip()
        DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DATABASE}"
        API_URL = "api"
    else:
        HOST = "database"
        PASSWORD = str(read_secret_file('/run/secrets/db-password')).strip()
        DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DATABASE}"
        API_URL = "https://api.econlabs.net"
    return [USER, PASSWORD, HOST, DATABASE, DATABASE_URL, SECRET_KEY, API_URL]

def read_secret_file(secret_path):
    with open(secret_path, 'r') as file:
        return file.read().strip()