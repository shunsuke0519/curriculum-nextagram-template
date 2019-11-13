from models.base_model import BaseModel
import peewee as pw
import datetime



class User(BaseModel):
    name = pw.CharField(unique=False)
    email = pw.CharField(unique=True)
    password = pw.CharField(unique=True)


