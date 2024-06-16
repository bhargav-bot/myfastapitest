from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional


class BHARGAV(BaseModel):
    name:str
    age:int
    id:int
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
    user_name:int
    pass_word:str
    class config:
        orm_mode=True

class Logininfo(BaseModel):
    username:str
    password:str
    class config:
        orm_mode=True


