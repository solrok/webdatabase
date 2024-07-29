import os
import pymysql
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from models import db, Job, Application

pymysql.install_as_MySQLdb()
load_dotenv()

app = Flask(__name__)

db_uri = os.getenv('SQLALCHEMY_DATABASE_URI')
track_modifications = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

print(f"Database URI: {db_uri}")
print(f"Track Modifications: {track_modifications}")

if not db_uri:
    raise RuntimeError("The SQLALCHEMY_DATABASE_URI environment variable is not set.")

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_modifications == 'True'

db.init_app(app)

@app.route('/')
def hello_world():
    jobs = Job.query.all()
    return render_template('home.html', jobs=jobs, company='xyz')

@app.route('/api/jobs')
def list_jobs():
    jobs = Job.query.all()
    return jsonify([{'id': job.id, 'title': job.title, 'location': job.location, 'salary': job.salary,
                     'currency': job.currency, 'responsibilities': job.responsibilities,
                     'requirements': job.requirements, 'created_at': job.created_at, 'updated_at': job.updated_at} for
                    job in jobs])

@app.route('/api/jobs/applications')
def list_applications():
    applications = Application.query.all()
    return jsonify([{'id': application.id, 'job_id': application.job_id, 'full_name': application.full_name, 'email': application.email,
                     'linkedin_url': application.linkedin_url, 'education': application.education,
                     'work_experience': application.work_experience, 'resume_url': application.resume_url, 'created_at': application.created_at, 'updated_at': application.updated_at} for
                    application in applications])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)