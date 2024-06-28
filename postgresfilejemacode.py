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




from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


while True:
   
    try:
        conn=psycopg2.connect(host='localhost',database=Settings.DATABASE_NAME,user=Settings.DATABASE_USERNAME,password=Settings.DATABASE_PASSWORD,port=5432,cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("database connection successful")
        print(Settings.DATABASE_HOSTNAME,Settings.DATABASE_NAME,Settings.DATABASE_USERNAME,Settings.DATABASE_PASSWORD)
        break
    except Exception as error:
        i=i+1
        print("database connection failed12")
        print(error)
        time.sleep(2)
        print("retrying")

        continue

bhargav12=FastAPI()
@bhargav12.get('/get12/')
def func1234():
    return "hello world"
@bhargav12.get('/')
def func23446wf3():
    try:
        cursor.execute("""SELECT * FROM table123""")
    except(Exception, psycopg2.DatabaseError) as error:
        # Rollback the transaction on error
        print("Error encountered:", error)
        conn.rollback()
    t=cursor.fetchall() 
    print(t)    
    return {'list':t}   




@bhargav12.get('/geto')
def func234463():
    try:
        cursor.execute("""SELECT * FROM table123""")
    except(Exception, psycopg2.DatabaseError) as error:
        # Rollback the transaction on error
        print("Error encountered:", error)
        conn.rollback()
    t=cursor.fetchall() 
    print(t)
    return {'list':t}

@bhargav12.post('/post12',status_code=status.HTTP_201_CREATED)
def func2456(var:BHARGAV):
    try:
        cursor.execute("""INSERT INTO table123 (name, age, id) VALUES (%s, %s, %s) returning *""",(var.name, var.age, var.id))
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        # Rollback the transaction on error
        print("Error encountered:", error)
        conn.rollback()
    d=cursor.fetchone()
    print(d)
    return {'list':d}
@bhargav12.delete("/delete12/{id}")
def fdh(id:int):
    try:
        cursor.execute("""delete from yourtable where id={} returning *""".format(id))
        conn.commit()
    except(Exception,psycopg2.DatabaseError) as error:
        print("Error encountered:", error)
        conn.rollback()

    d=cursor.fetchone()
    if d is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="there is no user with this id")
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
@bhargav12.put('/update/{id}')
def func2324(var:BHARGAV,id:int):
    try:
        cursor.execute("""UPDATE yourtable SET name = '{}', age = {} WHERE id = {} RETURNING *""".format(var.name, var.age, id))
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        # Rollback the transaction on error
        print("Error encountered:", error)
        conn.rollback()
    d=cursor.fetchone()
    print(d)
    if d is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="there is no user with this id")
    else:
        print("updated list is {}".format(d))
    return {'list':d}