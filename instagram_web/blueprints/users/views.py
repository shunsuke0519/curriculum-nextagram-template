from flask import Blueprint, render_template, url_for, request, flash, redirect
from models.user import User

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
    user_password = request.form.get("password")


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

