from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

from app import routes