from models.base_model import BaseModel
import peewee as pw
import datetime
from flask_login import UserMixin

# class User(BaseModel):
#     name = pw.CharField(unique=False)
#     email = pw.CharField(unique=True)
#     password = pw.CharField(unique=True)

class User(UserMixin, BaseModel):
    name = pw.CharField(unique=False)
    password = pw.CharField()
    email = pw.CharField(unique=True)


    def validate(self):
        duplicate_username = User.get_or_none(User.name == self.name)
        duplicate_email = User.get_or_none(User.email == self.email)

        if duplicate_username :
            self.errors.append("Username not unique")
        if duplicate_email :
            self.errors.append("Email not unique")
        # if len(self.password) < 6 or len(self.password) > 25:
        #     self.errors.append('Password must between 6-25 characters')
        # else:
        #     self.password=generate_password_hash(self.password)

    def is_authenticated(self):
        return True




