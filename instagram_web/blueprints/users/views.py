from flask import Blueprint, render_template, url_for


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')

# /usres/new
@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')
# render_template is for you to display html file

# /users/
@users_blueprint.route('/', methods=['POST'])
def create():
    pass
# Form date is sent to this route
# Gets data and create a new user

#Get form data
@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass

# username = request.form.get('username')

#Get email
#Get the password

#Create a new user from that deta
#Use peewee to create a new instance of a user
# Save it inside db

    # return redirect(url_for('users.new'))


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
