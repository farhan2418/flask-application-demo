from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__,static_folder='static', static_url_path='/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app,db)