import os

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, MetaData, Table

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
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
metadata_obj = MetaData()


class Base(DeclarativeBase):
    pass


class TestTable(Base):
    __table__ = Table(DB_TABLE, metadata_obj, autoload_with=engine)

# celery_test_table = Table(DB_TABLE, metadata_obj, autoload_with=engine)
