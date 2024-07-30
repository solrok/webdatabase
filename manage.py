import os
import pymysql
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from models import db

pymysql.install_as_MySQLdb()
#load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    from flask.cli import FlaskGroup
    cli = FlaskGroup(app)
    cli()