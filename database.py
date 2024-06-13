from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings
SQL_ALCHEMY_DATABASE_URL = 'postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}:5432/{Settings.database_name}'


engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close