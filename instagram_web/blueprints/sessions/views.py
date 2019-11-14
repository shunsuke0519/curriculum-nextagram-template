from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_user
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import logout_user

sessions_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates')

@sessions_blueprint.route('/'), methods=[GET]
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login/new')
    return render_template('entries/index.html')


# you dont need this because you specify it with @sessinos_blueprint
# @sessions_blueprint.route('/')
# def show_entries():
#     if not session.get('logged_in'):
#         return redirect('/login/new')
#     return render_template('entries/index.html')


@sessions_blueprint.route('/', methods=['POST'])
def create():
    user_email = request.form.get("email")
    user_name = request.form.get("name")
    password = request.form.get("password")
    if user:
        if check_password_hash(user.password, request.form.get('password')) :
            login_user(user) # store user id in session
            return redirect(url_for('users.show')) # redirect to profile page
        else:
            # password not matched
            return redirect(url_for('users/new.html'))
    else:
      # no user found in database
        return redirect(url_for('users/new.html'))


@sessions_blueprint.route('/delete',methods=['POST'])
@login_required
def destroy():
    logout_user()
    return redirect(url_for('sessions.new'))

