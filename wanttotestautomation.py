from fastapi import FastAPI, Request, Response, status, HTTPException, Depends, Form, UploadFile, File,Header
from sqlalchemy.orm import Session
from database import *
from jose import JWTError, jwt
from fastapi.responses import HTMLResponse
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import psycopg2
from psycopg2.extras import RealDictCursor
from time import time
from schemas import BHARGAV,PATEL,Logincredentials,Logininfo
from fastapi.middleware.cors import CORSMiddleware

from model import User12,Logininfo
import time,datetime
from starlette.responses import RedirectResponse
import model
from config import Settings
import random, string



from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


while True:
   
    try:
        conn=psycopg2.connect(host="localhost",database="bhargav",user='bhargav',password="YESHA1496",port=5432,cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("database connection successful")
        print(Settings.DATABASE_HOSTNAME,Settings.DATABASE_NAME,Settings.DATABASE_USERNAME,Settings.DATABASE_PASSWORD)
        break
    except Exception as error:
       
        print("database connection failed12")
        print(error)
        time.sleep(2)
        print("retrying")

        continue


timestamp=datetime.datetime.utcnow()
app=FastAPI()
templates = Jinja2Templates(directory="templates")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
genders=['male','female']

countries=['India','USA','UK','Australia','Canada','Germany','France','Italy','Spain','Japan','China']
for num in range(1,200):
    name=''.join(random.choices(string.ascii_letters, k=6))
    id=random.randint(200, 302)
    gender=random.choice(genders)
    country=random.choice(countries)
    cursor.execute("""select id from schedule where id=%s """,(id,))
    var2=cursor.fetchone()
    if id==var2:
        print("id already exists")
        continue
    else:
        try:
            cursor.execute("""INSERT INTO schedule (name,id,country,gender,unique_id) VALUES (%s,%s,%s,%s) on conflict do nothing""",(name,id,country,gender))
            conn.commit()
            print(f"Data inserted successfully:{name},{id}")
        except Exception as error:
            print("Data insertion failed")
            print(error)
            conn.rollback()

for num in range(1, 200):
    user_id=random.randint(200, 302)
    age=random.randint(18, 65)
    try:
        cursor.execute("""INSERT INTO inrelationwithschedule (user_id, age) VALUES (%s, %s) on conflict do nothing""", (user_id, age))
        conn.commit()
        print(f"Data inserted successfully:{user_id}, {age}")
    except Exception as error:
        print("Data insertion failed")
        print(error)
        conn.rollback()    

    conn.commit()



    
