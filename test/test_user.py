from fastapi.testclient import TestClient
from postgresfilejemacode import bhargav12
from mainfilejemacode import bhargav

import json
import pytest
client = TestClient(bhargav12)
client1=TestClient(bhargav)
def test_root():
    response=client.get("/get12")
    print(response.json())
    assert response.status_code == 200



def test_login():
    response=client1.post("/login",data={"username":543,"password":"1234"})

    assert response.status_code == 200


def test_signup():
    response=client1.post("/signup", data={"username":5443423, "password":"1234"})

    assert response.status_code ==201