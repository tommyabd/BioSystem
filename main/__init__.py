from http.client import ImproperConnectionState
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect


app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FlashRequest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5209a08cfb7acebb31ae9915' 
db = SQLAlchemy(app)
migrate = Migrate(app,db)
csrf = CSRFProtect(app)
Bootstrap(app)

from main import routes