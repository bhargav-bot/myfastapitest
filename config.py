from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    database_hostname:str=os.getenv("database_hostname")
    database_password:str=os.getenv("database_password")
    database_name:str=os.getenv("database_name")
    database_username:str=os.getenv("database_username")

    secret_key:str=os.getenv("secret_key")
    algorithm:str=os.getenv("algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES:int=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


    class Config:
        env_file = ".env"

Settings = Settings()


