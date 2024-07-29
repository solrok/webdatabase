from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

class Job(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    salary = db.Column(db.Integer)
    currency = db.Column(db.String(10))
    responsibilities = db.Column(db.String(2000))
    requirements = db.Column(db.String(2000))
    created_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))

class Application(db.Model):
    __tablename__ = "applications"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_id = db.Column(db.Integer, nullable=False)
    full_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    linkedin_url = db.Column(db.String(250), nullable=False)
    education = db.Column(db.String(2000))
    work_experience = db.Column(db.String(2000))
    resume_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))