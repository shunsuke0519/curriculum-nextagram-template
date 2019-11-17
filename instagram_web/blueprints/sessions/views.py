from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user import *
from werkzeug.security import check_password_hash
import time
from flask_login import current_user, login_user, logout_user, LoginManager, login_required

sessions_blueprint = Blueprint('sessions',
                             __name__,
                             template_folder='templates')




@sessions_blueprint.route('/signin', methods=['GET'])
def sign_in():
     return render_template('sessions/sign_in.html')

#############################
 # Option 1 : Session method #
 #############################


@sessions_blueprint.route('/signin', methods=['POST'])
def handle_sign_in():

     username = request.form.get("username")
     password = request.form.get("password")
     user = User.get_or_none(username=username)

     if user:
         result = check_password_hash(user.password, password)

         if result:
            flash("You are logged in", "success")
            #  session["user_id"] = user.id
            login_user(user)

            return redirect("/")

         else:
             flash("Log in fail, please try again", "danger")
             return render_template('sessions/sign_in.html')

     else:
         pass
         flash("Username or Password is incorrect. Please try again", "danger")
         return render_template('sessions/sign_in.html')

#################################
 # Option 2 : Flask-Login method #
 #################################

@sessions_blueprint.route('/signout')
@login_required
def handle_sign_out():
    logout_user()
    flash("You have successfully logged out", "success")
    return redirect(url_for('sessions.sign_in'))