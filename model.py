from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import null, true
from sqlalchemy.sql.sqltypes import Boolean
from database import Base
from sqlalchemy import DateTime, Integer, String

class User12(Base):
    __tablename__='User12'
    name=Column(String,nullable=False)
    user_id=Column(Integer,nullable=False,primary_key=True)
    surname=Column(String,nullable=False,default="Patel")
