from models.base_model import BaseModel
import peewee as pw
import datetime
from flask_login import UserMixin

# class User(BaseModel):
#     name = pw.CharField(unique=False)
#     email = pw.CharField(unique=True)
#     password = pw.CharField(unique=True)

class User(UserMixin, BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField(null=True, unique=True)
    password = pw.CharField(null=False)
    role = pw.CharField(default="user")


    def validate(self):
        duplicate_useremail = User.get_or_none(User.email == self.email)
        
        if duplicate_useremail:
            self.errors.append("Email has been taken. Please try another email.")




        # duplicate_email = User.get_or_none(User.email == self.email)

        # if duplicate_username :
        #     self.errors.append("Username not unique")
        # if duplicate_email :
        #     self.errors.append("Email not unique")
        # if len(self.password) < 6 or len(self.password) > 25:
        #     self.errors.append('Password must between 6-25 characters')
        # else:
        #     self.password=generate_password_hash(self.password)


    # def is_authenticated(self):
    #     return True




