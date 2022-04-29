from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
#from project import routes

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'authlog.login_page'
login_manager.init_app(app)		

from .model import User

@login_manager.user_loader
def load_user(user_id):
# поскольку идентификатор пользователя - это просто первичный ключ нашей таблицы пользователей, используйте его в запросе для пользователя
    return User.query.get(int(user_id))

from .mainlog import mainlog as mainlog_blueprint
app.register_blueprint(mainlog_blueprint)

from .authlog import authlog as authlog_blueprint
app.register_blueprint(authlog_blueprint)
