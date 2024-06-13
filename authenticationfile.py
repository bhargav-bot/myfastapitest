from jose import JWTError, jwt
from datetime import datetime,timedelta
from fastapi import Depends,status,HTTPException
from fastapi.security import oauth2,OAuth2PasswordBearer,OAuth2PasswordRequestForm
from mainfilejemacode import BHARGAV
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')
from time import time,sleep
from datetime import time,timedelta
import psycopg2
from psycopg2.extras import RealDictCursor
from jwt.exceptions import InvalidTokenError


while True:
    try:
        conn=psycopg2.connect(host='localhost',database='postgres',user='bhargav',password='YESHA1496',port='5431',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("database connection successful")
        break
    except Exception as error:
        print("database connection failed12")
        print(error)        
        time.sleep(2)
        print("retrying")
        continue

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 2

def genratetoken(dat:dict):

    to_encode=dat.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    exp=to_encode.get('exp')
    print(exp)
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    var = BHARGAV(**dat)
    getvalues(var,token)
    print("expire time is {}".format(expire))
    return token
def check_token(token:str=Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp = payload.get('exp')
        
        print(datetime.utcfromtimestamp(exp))
        print(datetime.utcnow())    

        
    except JWTError as e :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    if datetime.utcnow() > datetime.utcfromtimestamp(exp):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    else:
        id=payload.get('id')
        if id is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='could not validate the credentials',headers={'WWW-Authenticate':'Bearer'})

        else:
            print("token is valid")
            return payload
'''
def checktoken(token:str):
    d=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    print(d)
    if d is None:
        return True
    else:
        return False

'''
def getvalues(var:BHARGAV,token:str):
    cursor.execute("""INSERT INTO tokencode (user_id, token, time) VALUES (%s, %s, %s)""", (var.id, token, datetime.utcnow()))
    conn.commit()
    
