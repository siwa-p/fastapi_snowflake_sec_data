import os
from dotenv import load_dotenv
import logging
import snowflake.connector
from sqlalchemy import create_engine
from sqlmodel import Session

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA_BRONZE')
SNOWFLAKE_ROLE = os.getenv('SNOWFLAKE_ROLE')

def get_snowflake_connection():
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA,
            role=SNOWFLAKE_ROLE
        )
        logger.info("Successfully connected to Snowflake.")
        return conn
    except Exception as e:
        logger.error(f"Failed to connect to Snowflake: {e}")
        raise e

SNOWFLAKE_URL = os.getenv("SNOWFLAKE_CONNECTION_STRING")

engine = create_engine(SNOWFLAKE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

# if __name__ == '__main__':
#     conn = get_snowflake_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT CURRENT_VERSION()")
#     print(cursor.fetchone())
#     cursor.close()
#     conn.close()