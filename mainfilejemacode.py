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
from schemas import BHARGAV,PATEL
from fastapi.middleware.cors import CORSMiddleware
from authenticationfile import genratetoken
from authenticationfile import check_token
from model import User12
import model
bhargav=FastAPI()
Base.metadata.create_all(bind=engine)


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

@bhargav.post('/login/')
def func2324325(var:dict):
    token=genratetoken(var)
    return "token is genrated:{}".format(token)

@bhargav.get("/current_time")
def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}


@bhargav.get('/get123/')
def func234463():
    cursor.execute("""SELECT * FROM yourtable""")
    t=cursor.fetchall() 
    print(t)
    return {'list':t}
@bhargav.get('/yesha/')
def func1223(db:Session=Depends(get_db),d=Depends(check_token)):
    e=db.query(model.User12).all()
    print(e)
    return {'list':e}
@bhargav.post('/get12345/')
def func234(d=Depends(check_token)):
    
    cursor.execute("""SELECT * FROM yourtable""")
    t=cursor.fetchall() 
    print(t)
    return {'list':t}
@bhargav.post('/mypost',status_code=status.HTTP_201_CREATED)
def dghth(var:PATEL,db:Session=Depends(get_db)):
    par=model.User12(name=var.name,user_id=var.user_id,surname=var.surname)
    db.add(par)
    db.commit()
    db.refresh(par)
    return {"li1st":par}

@bhargav.put('/update2/{id}')
def funcwegwg(id:int,var:PATEL,db:Session=Depends(get_db)):
    db.query(model.User12).filter(model.User12.user_id==id).update(var.dict())
    d=db.query(model.User12).all()
    return d



@bhargav.post('/post12',status_code=status.HTTP_201_CREATED)
def func2456(var:BHARGAV):
    cursor.execute("""INSERT INTO yourtable (name, age, id) VALUES (%s, %s, %s) returning *""",(var.name, var.age, var.id))
    conn.commit()
    d=cursor.fetchone()
    print(d)
    return {'list':d}
@bhargav.delete("/delete12/{id}")
def fdh(id:int):
    cursor.execute("""delete from yourtable where id={} returning *""".format(id))
    conn.commit()
    d=cursor.fetchone()
    if d is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="there is no user with this id")
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
@bhargav.put('/update/{id}')
def func2324(var:BHARGAV,id:int):
    cursor.execute("""UPDATE yourtable SET name = '{}', age = {} WHERE id = {} RETURNING *""".format(var.name, var.age, id))
    conn.commit()
    d=cursor.fetchone()
    print(d)
    if d is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="there is no user with this id")
    else:
        print("updated list is {}".format(d))
    return {'list':d}
@bhargav.delete("/del/{id}",status_code=status.HTTP_204_NO_CONTENT)
def fergerf(id:int,db:Session=Depends(get_db)):
    db.query(model.User12).filter(model.User12.user_id==id).delete()
    db.commit()
    



    

my_list=[{'name':'bhargav','age':21,'subject':'python'}]

def printlist():
    print(my_list)
printlist()
@bhargav.get("/get")
def func():
    return {'list':my_list}


@bhargav.post("/post",status_code=status.HTTP_201_CREATED)
def func1(var:dict):
    my_list.append(var)
    return {'list':my_list}
def finduserindex(age:int):
    for i,j in enumerate(my_list):
        if j['age']==age:
            print(i)
            return i
        else:
            continue


@bhargav.delete("/delete/{age}",status_code=status.HTTP_204_NO_CONTENT)
def func2(age:int):
    d=finduserindex(age)
    print(d)
    if d is not None:
        my_list.pop(d)
        print(my_list)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found ')
    return {'list':my_list}
