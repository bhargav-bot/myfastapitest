from fastapi.testclient import TestClient
from postgresfilejemacode import bhargav12
from mainfilejemacode import bhargav
from schemas import BHARGAV,BHARGAV12
import requests
import json
import pytest
from sqlalchemy import create_engine
from config import Settings
from sqlalchemy.orm import sessionmaker
from database import get_db,Base
from sqlalchemy.ext.declarative import declarative_base



SQL_ALCHEMY_DATABASE_URL = f'postgresql://{Settings.DATABASE_USERNAME}:{Settings.DATABASE_PASSWORD}@localhost:{Settings.database_port1}/test'
print(SQL_ALCHEMY_DATABASE_URL)
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
test_sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db_test():
    try:
        db = test_sessionlocal()
        yield db
    finally:
        db.close()  

@pytest.fixture
def test_user(client1):
    user_data = {"username": 1908, "password": "giyanhaiaap"}
    response=client1.post("/signup", data=user_data)
    assert response.status_code == 200
    return user_data



@pytest.fixture()
def session():
    print("my session module is runnning")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = test_sessionlocal()
    try:
        yield db
    finally:
        db.close()
    


@pytest.fixture()
def client(session):
    def get_db_test():
            
        try:              
            yield session
        finally:
            session.close()
    bhargav.dependency_overrides[get_db]=get_db_test
    yield TestClient(bhargav12)

bhargav.dependency_overrides[get_db]=get_db_test


@pytest.fixture()
def client1(session):
    def get_db_test():
            
        try:              
            yield session
        finally:
            session.close()
    bhargav.dependency_overrides[get_db]=get_db_test
    yield TestClient(bhargav)

@pytest.fixture
def gettoken(client1,test_user):
    user_data = {"name": "Bharagv", "age": 22,"id":4422}
    response=client1.post("/login12", json=user_data)
    #print("response:::"+str(response.json()))
    assert response.status_code == 200
    return response.json()["token"]
@pytest.fixture
def gettoken1(client1,test_user):
    user_data = {"name": "Bharagv1", "age": 22,"id":44322}
    response=client1.post("/login12", json=user_data)
    print("response:"+str(response))
    assert response.status_code == 200
    return response



@pytest.fixture
def athoriziedclient(test_user):
    response=client1.post('/login12',json=test_user)
    return

