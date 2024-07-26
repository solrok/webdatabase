import pymysql

pymysql.install_as_MySQLdb()
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text

app = Flask(__name__)

# Configure the MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://local:d%21tcs%23%40Noc%40%34321@localhost/JObS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Define your database model
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

class application(db.Model):
    __tablename__ = "applications"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    job_id= db.Column(db.Integer, nullable=False)
    full_name= db.Column(db.String(250), nullable=False)
    email= db.Column(db.String(250), nullable=False)
    linkedin_url= db.Column(db.String(250), nullable=False)
    education = db.Column(db.String(2000))
    work_experience= db.Column(db.String(2000))
    resume_url=db.Column(db.String(500))
    created_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))


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
def list_applictions():
    applications = application.query.all()
    return jsonify([{'id': application.id, 'job_id': application.job_id, 'full_name': application.full_name, 'email': application.email,
                     'linkedin_url': application.linkedin_url, 'education': application.education,
                     'work_experience': application.work_experience, 'resume_url':application.resume_url,'created_at': application.created_at, 'updated_at': application.updated_at} for
                    application in applications])
print(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
