from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional


class BHARGAV(BaseModel):
    name:str
    age:int
    id:int
    class config:
        orm_mode=True
class BHARGAV12(BaseModel):
    name:str
    age:int
    id:int
    token:str
    class config:
        orm_mode=True


class PATEL(BaseModel):
    name:str
    user_id:int
    surname:str
    class config:
        orm_mode=True
class any(BaseModel):
    name:str

class Logincredentials(BaseModel):
    username:int
    password:str
    class config:
        orm_mode=True
        orm_mode=True

class Logininfo(BaseModel):
    username:int
    password:str
    class config:
        orm_mode=True


class Login123(BaseModel):
    username:str
    email:str
    password:str
    class config:
        orm_mode=True


