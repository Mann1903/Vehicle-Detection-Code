import warnings
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'qazwsxedcrfvtgbyhnujmiklop12345678'

app.config['SQLALCHEMY_ECHO'] = True

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root%401234@localhost:3306/vehicle_detection?charset=utf8'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)
from base.com import controller