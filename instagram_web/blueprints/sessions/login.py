from flask import Blueprint, render_template, url_for, request, flash


users_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/', methods=['POST'])
def create():
    users_name = request.form.get("username")
    users_email = request.form.get("email")
    users_password = request.form.get("password")


    return render_template('users/new.html',
        users_name = request.form.get("username"),
        users_email = request.form.get("email"),
        users_password = request.form.get("password"))
