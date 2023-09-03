# Celery vs. gRPC in microservices-based architecture

 TODO

# SQLAlchemy reflection

As it is understood by the author there are actually two approaches to reflect DB structure with SQLAlchemy. Here are two examples on how to do that.

<details>
<summary>non-ORM approach</summary>

In this approach it is not necessary to use SQLAlchemy ORM in order to reflect DB and run statements against it.

```python
import os

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
metadata_obj = MetaData()
metadata_obj.reflect(engine, only=[DB_TABLE])

test_table = Table(DB_TABLE, metadata_obj, autoload_with=engine)

# Execute insert statement
with engine.connect() as conn:
    conn.execute(
        test_table.insert().values(
            col_1="val_1",
            col_2="val_2",
            col_3="val_3",
        )
    )
    conn.commit()
```

</details>
</br>

<details>
<summary>ORM approach</summary>

In this approach you can use SQLAlchemy ORM in order to reflect DB and run statements against it.

```python
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


# Execute insert statement
db_session.add(
    TestTable(
        col_1="value_1",
        col_2="value_2",
        col_3="value_3"
    )
)
db_session.commit()
db_session.remove()
```

When using Celery this can be used as:

```python
class SqlAlchemyTask(Task):
    """
    An abstract Celery Task that ensures that the connection to the
    database is closed on task completion.
    """
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        db_session.remove()


@app.task(base=SqlAlchemyTask, bind=True, name=MAIN_TASK, queue=MAIN_QUEUE)
def task(self, *args, **kwargs) -> dict:
    """Task to execute insert statement."""
    db_session.add(TestTable(col_1="value_1", col_2="value_2", col_3="value_3"))
    db_session.commit()
    return result
```

</details>
</br>