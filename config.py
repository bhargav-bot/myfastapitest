from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname:str='c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com'
    
    database_password:str='pfc2fb6bc2755d68700ca31d31c66e5f966621007d1bf721338a4544d868755f6'
    database_name:str='d7tfu32ti1me77'
    database_username:str='uegsmsrkgaomm8'
    secret_key:str= '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
    algorithm:str= 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES:int= 30

    class Config:
        env_file = ".env"

Settings = Settings()

