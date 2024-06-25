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
    var= response.json()
    return var



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


def test_root(client):
    response=client.get("/get12")
    print(response.json())
    assert response.status_code == 200
'''

def test_signup(client1):
    response=client1.post("/signup", data={"username":54454323, "password":"1234"})

    assert response.status_code ==200

def test_signup1(client1):
    response=client1.post("/signup", data={"username":544454323, "password":"1234"})

    assert response.status_code ==200
    '''
def test_login(client1,test_user):
    response=client1.post("/login/",data={"username":test_user['username'],"password":test_user['password']})
    assert response.status_code == 200



def test_login12(client1):
    response=client1.post("/login12", json={"name":"ketan", "age":43,"id":345365})
    
    info = BHARGAV12(**response.json())
    assert response.status_code == 200
    assert info.name == "ketan"
    assert info.age == 43
    assert info.id == 345365

def test_ifo(client1):
    response=client1.get("/getinfo")
    print(response.json())
    assert response.status_code == 200
'''
def test_heroku():
    url='https://bhargav-api-6b3bcd214c72.herokuapp.com/getinfo/'
    response=requests.get(url)
    print(response.json())
    '''