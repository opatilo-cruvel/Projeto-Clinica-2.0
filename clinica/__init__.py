from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

database = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e130616980c3ea8d297d37ca384b9260'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2{U|Ny9_\\5sV@localhost:5432/teste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database.init_app(app)  # Inicializa a instância de database que vem de models.py
bcrypt = Bcrypt(app)

from clinica import routes
