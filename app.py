import os
import pymysql
from flask import Flask, render_template, jsonify , request
from dotenv import load_dotenv
from models import db, Job, Application
from database import load_job_from_db , load_job_from_id , add_application_db
pymysql.install_as_MySQLdb()
#load_dotenv()

app = Flask(__name__)

db_uri = os.getenv('SQLALCHEMY_DATABASE_URI')
track_modifications = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'

# print(f"Database URI: {db_uri}")
# print(f"Track Modifications: {track_modifications}")

if not db_uri:
    raise RuntimeError("The SQLALCHEMY_DATABASE_URI environment variable is not set.")

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_modifications == 'True'

db.init_app(app)

@app.route('/')
def hello_world():
    #jobs = Job.query.all()
    jobs =load_job_from_db()
    return render_template('home.html', jobs=jobs, company='xyz')
    #return render_template('home.html',  company='xyz')
@app.route('/api/jobs')
def list_jobs():
    jobs = load_job_from_db()
    return jsonify(jobs)
@app.route("/job/<id>")
def show_job(id):
    job=load_job_from_id(id)
    if not job:
        return "NOT Found", 404
    return render_template('jobpage.html',job=job)


@app.route("/jobs/<id>/apply", methods=['POST'])
def apply_job(id):
    data = request.form
    job = load_job_from_id(id)
    add_application_db(id, data)
    return render_template('application_submited.html', application=data, job=job)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)