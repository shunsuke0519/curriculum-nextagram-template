from flask import Blueprint, render_template, url_for, request, flash, redirect
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
import re

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')

# /usres/new
@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')
# render_template is for you to display html file

# /users/
#Get email
#Get the password
#Create a new user from that deta
#Use peewee to create a new instance of a user
# Save it inside db

@users_blueprint.route('/', methods=['POST'])
def create():
    user_email = request.form.get("email")
    user_name = request.form.get("name")
    password = request.form.get("password")
    # hashed_password = generate_password_hash(password) # store this in database
    # user_password = hashed_password
    user_password = generate_password_hash(password)

    if len(user_password) < 6 :
        flash("Password must be more than 6 characters !", "danger")
        return render_template('users/new.html')
    elif not re.search(r"([A-Z]+[a-z]+|[a-z]+[A-Z]+)", user_password):
        flash("Password must contain at least one(1) upper and one(1) lower case", "danger")
        return render_template('users/new.html')
    elif not re.search(r"[!@#0^&*()+]+", user_password):
        flash("Password must contain at least one(1) special character", "danger")
        return render_template('users/new.html')
    
    # user_hashed_password = generate_password_hash(user_password)


    new_user = User(
        email=user_email,
        name=user_name,
        password=user_password)

        
    # return render_template('users/new.html',
    #     email = request.form.get("email"),
    #     usersname = request.form.get("name"),
    #     password = request.form.get("password"))

    if new_user.save():
        print("Successfully signed up !", "success")
        return redirect(url_for('users.new'))
    else:
        return render_template('users/new.html', error=new_user.errors)


#Get form data
@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass




@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass

