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
from schemas import BHARGAV,PATEL,Logincredentials,Logininfo,BHARGAV12,Login123,contact12
from authenticationfile import genratetoken
from authenticationfile import check_token
from model import User12,Logininfo,contact
import time,datetime
from starlette.responses import RedirectResponse
import model
from fastapi.responses import HTMLResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
import mailersend
from mailersend import emails
api_key = "mlsn.43f1eaa97a620bfdb525476088b80d3c481a15d12a5e50b708bf34e00ff9eaec"
mailer = emails.NewEmail(api_key)
current_time1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#this is the change i am adding to my file to check if the change is execuated on my server 

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


bhargav=FastAPI()
Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")




conf=ConnectionConfig(
    MAIL_USERNAME="bhargavp1219@yahoo.com",
    MAIL_PASSWORD="Yesha@1496",
    MAIL_FROM="bhargavp1219@yahoo.com",
    MAIL_PORT=587,  # Yahoo SMTP port
    MAIL_SERVER="smtp.mail.yahoo.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False
)

@bhargav.get('/')
def myfunc():
    return "hello world"

@bhargav.get("/login", response_class=HTMLResponse)
def show_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@bhargav.post("/login")
def login(request: Request, username: int = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(Logininfo).filter(Logininfo.username == username).first()
    print("user :{}".format(user))
    if user is None or user==0  :
        return templates.TemplateResponse("404.html", {"request": request},status_code=status.HTTP_404_NOT_FOUND)
        exit
    elif user is not None and user.password != password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    else:
        return RedirectResponse(url="/welcome", status_code=status.HTTP_302_FOUND)

@bhargav.get("/welcome", response_class=HTMLResponse)
def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

@bhargav.get("/signup", response_class=HTMLResponse,status_code=status.HTTP_201_CREATED)
def show_signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@bhargav.post("/signup",status_code=status.HTTP_201_CREATED)
def signup(request: Request, username:int=Form(...),password:str=Form(...), db: Session = Depends(get_db)):
    var=Logininfo(username=username,password=password)
    db.add(var)
    db.commit()
    db.refresh(var)
    return templates.TemplateResponse("signupsuccesful.html", {"request": request,'username':username})

    
@bhargav.delete("/del/{id}",status_code=status.HTTP_204_NO_CONTENT)
def fergerf(id:int,db:Session=Depends(get_db)):
    db.query(model.User12).filter(model.User12.user_id==id).delete()
    db.commit()

@bhargav.post('/login12/')
def func2324325(var:dict):
    token=genratetoken(var)
    var12=BHARGAV(**var)
    finalvar=BHARGAV12(name=var12.name,age=var12.age,token=token,id=var12.id)
    return finalvar

@bhargav.get("/current_time")
def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}

@bhargav.get('/authlog')
def func232235(db:Session=Depends(get_db), d=Depends(check_token)):
    e=db.query(model.Logininfo).all()
    return e
#hi

@bhargav.get('/yesha/')
def func1223(db:Session=Depends(get_db),d=Depends(check_token)):
    e=db.query(model.User12).all()
    print(e)
    return {'list':e}

@bhargav.get('/getinfo/')
def func12232(db:Session=Depends(get_db)):
    e=db.query(model.User12).all()

    return e

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
  

my_list=[{'name':'bhargav','age':21,'subject':'python'}]

def printlist():
    print(my_list)

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
'''

        '''



@bhargav.get('/gettime/')
def func432():
    return RedirectResponse("https://www.utctime.net/utc-timestamp.net")


@bhargav.get('/home',response_class=HTMLResponse)
def func1232(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@bhargav.post('/home')
def func1211(request: Request, username:str=Form(...),password:str=Form(...),db:Session=Depends(get_db)):
    var=db.query(model.LoginDatabase).filter(model.LoginDatabase.username==username).first()
    
    print(var.password)
    print(type(var.username))
    if var is None or var==0:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=status.HTTP_404_NOT_FOUND)
    if var.password!=password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    else:
        return templates.TemplateResponse("welcome.html", {"request": request})
    
@bhargav.get('/signuphome',response_class=HTMLResponse)
def func12123(request: Request):
    return templates.TemplateResponse("signuphome.html", {"request": request})

@bhargav.post('/signuphome', status_code=status.HTTP_201_CREATED)
def func2324232(request: Request, username:str=Form(...), password:str=Form(...),email:str=Form(...), db:Session=Depends(get_db)):
    var=model.LoginDatabase(username=username, password=password,email=email)
    print(type(var.username))
    db.add(var)
    db.commit()
    db.refresh(var)
    return templates.TemplateResponse("signupsuccesfulhome.html", {"request": request, 'username':username})
from datetime import datetime
@bhargav.get('/contact',response_class=HTMLResponse)
def func12321(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})


@bhargav.post('/contact')
async def func121212(request: Request, name:str=Form(...), email:str=Form(...), message:str=Form(...),db:Session=Depends(get_db)):

    var=model.contact(name=name, email=email, message=message)
    db.add(var)
    db.commit()
    db.refresh(var)


    # Define email parameters
    mail_body = {}
    mail_from = {
        "email": "Bhargavpatel@patels.online",
    }
    recipients = [
        {
            "email": "bhargavp19082002@gmail.com",  # Replace with the actual recipient's email
        }
    ]

    # Set email attributes
    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("New Contact Form Submission:{current_time1}", mail_body)
    mailer.set_html_content(f"<p>Name: {name}</p><p>Email: {email}</p><p>Message: {message}</p>", mail_body)
    #mailer.set_plaintext_content(f"Name: {name}\nEmail: {email}\nMessage: {message}", mail_body)

    mailer.send(mail_body)
    print(mailer.send(mail_body))

@bhargav.get('/getcontact')
def func123212(db:Session=Depends(get_db)):
    e=db.query(model.contact).all()
    return e




    
'''    message = MessageSchema(
    subject="Thank you for your message",  # Ensure subject is a string
    recipients=["760041bp@gmail.com"],    # Replace with your actual recipients
    body=f"Name: {var.name}\nEmail: {var.email}\n\nMessage:\n{var.message}",
    subtype="plain"  # Add the subtype field with an appropriate value

        fm = FastMail(conf)
    await fm.send_message(message)

)'''