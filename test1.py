from sqlalchemy import create_engine, text
import os
import pymysql
from dotenv import load_dotenv
load_dotenv()
pymysql.install_as_MySQLdb()
# Create an engine
engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
from sqlalchemy.exc import SQLAlchemyError
# SQL statement
sql = text("""
    INSERT INTO JObS.applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
    VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
""")

# Data to insert
data = {
    'job_id': 1,
    'full_name': 'Bruce Wayne',
    'email': 'Bruce@wayne.com',
    'linkedin_url': 'https://linkedin.com/in/brucewayne',
    'education': 'Masters in Business Administration',
    'work_experience': '5 years at Wayne Enterprises',
    'resume_url': 'https://example.com/resume.pdf'
}

# Execute the statement
try:
    with engine.connect() as conn:
        result = conn.execute(sql, data)
        print("Insert successful:", result.rowcount)
except SQLAlchemyError as e:
    print(f"Error inserting data: {e}")