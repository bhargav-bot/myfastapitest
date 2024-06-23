from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    database_hostname1: str = os.getenv("database_hostname1")
    database_password1: str = os.getenv("database_password1")
    database_name1: str = os.getenv("database_name1")
    database_username1: str = os.getenv("database_username1")
    secret_key1: str = os.getenv("secret_key1")
    algorithm1: str = os.getenv("algorithm1")
    access_token_expire_minutes1: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    database_port1: str = os.getenv("database_port")
    DATABASE_HOSTNAME: str = os.getenv("DATABASE_HOSTNAME")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
    DATABASE_USERNAME: str = os.getenv("DATABASE_USERNAME")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    DATABASE_PORT: str = os.getenv("DATABASE_PORT")
    class Config:
        env_file = ".env"



Settings = Settings()


