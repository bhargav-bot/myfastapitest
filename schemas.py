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

class contact12(BaseModel):
    name:str
    email:str
    message:str
    class config:
        orm_mode=True

class ConnectionConfig(BaseModel):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: Optional[str] = None
    MAIL_PORT: Optional[int] = None
    MAIL_SERVER: Optional[str] = None
    MAIL_TLS: Optional[bool] = True  # Example: Set to True for TLS
    MAIL_SSL: Optional[bool] = False  # Example: Set to True for SSL
    USE_CREDENTIALS: bool = True