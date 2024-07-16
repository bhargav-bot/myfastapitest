from fastapi import FastAPI,Depends,Request,Form,status
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from fastapi import status,HTTPException
from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional
from fastapi.templating import Jinja2Templates
from sqlalchemy import ForeignKey
from typing import List
from fastapi.responses import RedirectResponse,HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

engine = create_engine("postgresql://bhargav:YESHA1496@localhost:5432/SERVERTEST")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class schedule(Base):
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)

class timetable(Base):
    __tablename__ = "timetable"
    user_id=Column(Integer, ForeignKey('schedule.id'))
    monday=Column(String, nullable=False,default="None")
    tuesday=Column(String, nullable=False,default="None")
    wednesday=Column(String, nullable=False,default="None")
    thursday=Column(String, nullable=False,default="None")
    friday=Column(String, nullable=False,default="None")
    rollno=Column(Integer, nullable=False,primary_key=True)
    class config:
        orm_mode=True


    

class User(BaseModel):
    id:int
    name:str
    age:int
    class config:
        orm_mode=True

class User2(BaseModel):
    user_id:int
    monday:str=Field(default="None")    
    tuesday:str=Field(default="None")
    wednesday:str=Field(default="None")
    thursday:str=Field(default="None")
    friday:str=Field(default="None")
    rollno:int
    class config:
        orm_mode=True
class timetable2(User2):
    User2:User2
    name:str
    age:int
    class config:
        orm_mode=True
Base.metadata.create_all(bind=engine)

@app.get("/get")
def read_root(db:Session=Depends(get_db)):
    e=db.query(schedule).all()
    return e


@app.post("/post",status_code=status.HTTP_201_CREATED)
def get_root12(var2:User,db:Session=Depends(get_db)):
    var=schedule(id=var2.id,name=var2.name,age=var2.age)
    db.add(var)
    db.commit()
    db.refresh(var)
    return var
@app.post("/postt", status_code=status.HTTP_201_CREATED)
def get_root(var2:User2,db:Session=Depends(get_db)):
    var=timetable(user_id=var2.user_id,monday=var2.monday,tuesday=var2.tuesday,wednesday=var2.wednesday,thursday=var2.thursday,friday=var2.friday,rollno=var2.rollno)
    db.add(var)
    db.commit()
    db.refresh(var)
    return var


@app.put("/update/{user_id}")
def update(user_id:int,var2:User,db:Session=Depends(get_db)):
    var=db.query(schedule).filter(schedule.id==user_id).first()
    if var==0 or var is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found')
    else:
        db.query(schedule).filter(schedule.id==user_id).update(var2.dict())
        db.commit()
        db.refresh(var)
        return var


@app.delete("/delete/{user_id}",status_code=status.HTTP_410_GONE)
def delete12(user_id:int,db:Session=Depends(get_db)):
    var=db.query(schedule).filter(schedule.id==user_id).first()
    if var==0 or var is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found')
    else:
        db.query(schedule).filter(schedule.id==user_id).delete()
    db.commit()
    return "userdeleted has been deleted"

@app.get("/geth",response_class=HTMLResponse)
def func(request:Request):
    return templates.TemplateResponse("firstweb.html",{"request":request})
from sqlalchemy import select
@app.get("/geth2")
def func23(db:Session=Depends(get_db)):
    #d=db.query(schedule).join(timetable,timetable.user_id==schedule.id,isouter=True).all()
    results = db.query(schedule, timetable).join(timetable, timetable.user_id == schedule.id, isouter=True).all()
    data = [dict(row._mapping) for row in results]
    return data
@app.get("/inner")
def func234543(db: Session = Depends(get_db)):
    query = select(schedule, timetable).join(timetable, timetable.user_id == schedule.id)
    results = db.execute(query)
    data = [{**row[0].__dict__, **row[1].__dict__} for row in results]
    return data
@app.get("/outer")
def func234543(db: Session = Depends(get_db)):
    query = select(schedule, timetable).join(timetable, timetable.user_id == schedule.id, isouter=True)
    results = db.execute(query)
    print(results)
    data = []
    for row in results:
        schedule_data = row[0].__dict__
        timetable_data = row[1].__dict__ if row[1] is not None else {}
        data.append({**schedule_data, **timetable_data})
    
    return data

@app.get("/leftouter")
def func2345433wr(db: Session = Depends(get_db)):
    query = select(schedule, timetable).outerjoin(timetable, timetable.user_id == schedule.id)
    results = db.execute(query)
    data = []
    for row in results:
        schedule_data = row[0].__dict__
        timetable_data = row[1].__dict__ if row[1] is not None else {}
        data.append({**schedule_data, **timetable_data})


    return data

@app.get("/rightouter")
def func2345433wr(db: Session = Depends(get_db)):
    query = select(timetable,schedule).outerjoin(schedule, timetable.user_id == schedule.id)
    print(query)
    print(select(timetable, schedule).outerjoin(timetable, timetable.user_id == schedule.id))
    results = db.execute(query)
    data = []
    for row in results:
        schedule_data = row[0].__dict__ if row[0] is not None else {}
        timetable_data = row[1].__dict__ if row[1] is not None else {} 
        data.append({**schedule_data, **timetable_data})


    return data

@app.get('/getall')
def func233(db:Session=Depends(get_db)):
    results = db.query(schedule, timetable).join(timetable, timetable.user_id == schedule.id, isouter=True).all()
    data=[]
    for row in results:
        schedule_data=row[0].__dict__ if row[0] is not None else {}
        timetable_data=row[1].__dict__ if row[1] is not None else {}
        data.append({**schedule_data, **timetable_data})
    return data

@app.get('/profile',response_class=HTMLResponse)
def func234asdfsadf(request:Request,db: Session = Depends(get_db)):
    variable=db.query(schedule).filter(schedule.id==15).first()
    return templates.TemplateResponse("profile.html", {"request":request ,"age":variable.age,"name":variable.name,"id":variable.id})

    

@app.get('/getto')
def fdsg(db:Session=Depends(get_db)):
    var=db.query(schedule,timetable).join(timetable,timetable.user_id==schedule.id).all()
    data=[]
    for row in var:
        var1=row[0].__dict__ if row[0] is not None else {}
        var2=row[1].__dict__ if row[1] is not None else {}
        data.append({**var1,**var2})
    return data


