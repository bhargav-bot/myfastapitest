from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings
#SQL_ALCHEMY_DATABASE_URL = 'postgresql://uegsmsrkgaomm8:pfc2fb6bc2755d68700ca31d31c66e5f966621007d1bf721338a4544d868755f6@c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d7tfu32ti1me77'
SQL_ALCHEMY_DATABASE_URL = f'postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}:{Settings.database_port}/{Settings.database_name}'


engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close