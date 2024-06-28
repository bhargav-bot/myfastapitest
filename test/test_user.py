from schemas import BHARGAV12
import requests
import pytest

def test_root(client):
    response=client.get("/get12")
    print(response.json())
    assert response.status_code == 200

def test_signup(client1):
    response=client1.post("/signup", data={"username":54454323, "password":"1234"})

    assert response.status_code ==200

def test_signup1(client1):
    response=client1.post("/signup", data={"username":544454323, "password":"1234"})

    assert response.status_code ==200
    '''
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
    assert response.status_code == 404

def test_heroku():
    url='https://bhargav-api-6b3bcd214c72.herokuapp.com/getinfo/'
    response=requests.get(url)
    print(response.json())
  



def test_authtoken(client1,gettoken,gettoken1):
    
    headers={
            "Authorization": f"Bearer {gettoken}"
        }
    response=client1.get('/authlog', headers=headers)
    print(gettoken1)
    assert response.status_code == 200

def test_root(client):
    response=client.get("/getinfo")
    print(response.json())
    assert response.status_code == 200

print('hello')

def test_check():
    assert 1==1