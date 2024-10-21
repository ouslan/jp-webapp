from dotenv import load_dotenv
import os

load_dotenv()


# Get the Database credentials
def get_db_credentials():
    PORT = os.getenv("POSTGRES_PORT")
    USER = os.getenv("POSTGRES_USER")
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    HOST = os.getenv("POSTGRES_HOST")
    DATABASE = os.getenv("POSTGRES_DB")
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")

    if not all([HOST, USER, PASSWORD, DATABASE, PORT, DATABASE_URL]):
        raise ValueError("Database credentials not set")
    if os.environ.get("DEV") == "True":
        HOST = "localhost"
        DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    else:
        HOST = "timescaledb"
        DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    return PORT, USER, PASSWORD, HOST, DATABASE, DATABASE_URL, SECRET_KEY
