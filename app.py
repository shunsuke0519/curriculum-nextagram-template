import os
import config
from flask import Flask
from models.base_model import db
from flask_login import UserMixin, LoginManager
from flask_wtf.csrf import CSRFProtect

# from flask_wtf.csrf import CSRFProtect


web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'instagram_web')

app = Flask('NEXTAGRAM', root_path=web_dir)


csrf = CSRFProtect(app)
login_manager = LoginManager()
login_manager.init_app(app)
# 3 lines are optional
# login_manager.login_view = "sessions.new" 
# login_manager.login_message = "Please log in before proceeding"
# login_manager.login_message_category = "warning"


if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id) # get id from session,then retrieve user object from database



@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
