from sqlmodel import SQLModel, create_engine

import models

sqlite_file_name = "database.db"

# On memory db when using only two backslash.
# sqlite_url = f"sqlite://{sqlite_file_name}"

# File db.
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False}, echo=True)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)
