import os

from sqlalchemy import MetaData, Table, create_engine

DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_TABLE = os.environ.get("DB_TABLE")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    pool_recycle=3600,
    pool_size=2,
    echo=False,
)
metadata_obj = MetaData()
metadata_obj.reflect(engine, only=[DB_TABLE])

test_table = Table(DB_TABLE, metadata_obj, autoload_with=engine)
