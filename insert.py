from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
from dotenv import load_dotenv
import os

from models import Job

pymysql.install_as_MySQLdb()
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
db = SQLAlchemy(app)
JOBS = [{
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 1000000,
    }, {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 1500000,
        'responsibilities': 'warngling',
    }, {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Remote',
        'salary': 1200000,
        'responsibilities': 'react',
    }, {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'San Francisco, USA',
        'responsibilities': 'framework',

    }]

with app.app_context():
    for job in JOBS:
        new_job = Job(
            id=job['id'],
            title=job['title'],
            location=job['location'],
            salary=job.get('salary'),
            currency=job.get('currency')
        )
        db.session.add(new_job)
        db.session.commit()
        print("jobs inserted successfully")