import os

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, UUID, TIMESTAMP

DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_TABLE = os.environ.get("DB_TABLE")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    convert_unicode=True,
    pool_recycle=3600,
    pool_size=10,
    echo=False,
)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


class Base(DeclarativeBase):
    pass


class TestString(Base):
    __tablename__ = DB_TABLE

    # id = Column("id", UUID, primary_key=True),
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    test_string: Mapped[str] = mapped_column(String(8192), nullable=False)
    worker: Mapped[str] = mapped_column(String(64), nullable=False)
    requested: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)
    added: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)

    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', password='%s')>" % (
    #         self.name,
    #         self.fullname,
    #         self.password,
    #     )


TestString.metadata.create_all(engine)

###

# metadata_obj = MetaData()
# celery_table = Table(
#     DB_TABLE,
#     metadata_obj,
#     Column("id", UUID, primary_key=True),
#     Column("test_string", String(8192), nullable=False),
#     Column("worker", String(64), nullable=False),
#     Column("requested", TIMESTAMP, nullable=False),
#     Column("added", TIMESTAMP, nullable=False)
# )
# metadata_obj.create_all(engine)

