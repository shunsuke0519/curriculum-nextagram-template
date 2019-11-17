from flask import Blueprint, render_template, url_for, request, flash, redirect, session
from flask_login import login_user
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import logout_user
from flask_login import login_user 
from instagram_web.util.google_oauth import oauth

sessions_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates')

@sessions_blueprint.route("/signin", methods=["GET"])
def sign_in():
    return render_template("sessions/sign_in.html")



@sessions_blueprint.route('/signin', methods=['POST'])
def handle_sign_in():

    username = request.form.get("username")
    password = request.form.get("password")
    user = User.get_or_none(username=username)

    if user:
        result = check_password_hash(user.password, password)
            
        if result:
            flash("You are logged in", "success")
            session["user_id"] = user.id 
            return redirect("/")

        else:
            flash("Login in fail, please try again", "danger")
            return render_template('sessions/sign_in.html')

    else:
        pass


@sessions_blueprint.route('/signout')
def handle_sign_out():
     session.pop('user_id', None)
     flash("You have successfully logged out", "success")
     return redirect(url_for('sessions.sign_in'))



# @sessions_blueprint.route('/delete',methods=['POST'])
# @login_required
# def destroy():
#     logout_user()
#     return redirect(url_for('sessions.new'))


# @sessions_blueprint.route('/login/google', methods=[GET])
# def google_login():
#     token = oauth.google.authorize_access_token()
#     email = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo').json()['email']

