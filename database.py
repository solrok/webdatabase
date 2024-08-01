from sqlalchemy import create_engine,text
import os
import pymysql
from dotenv import load_dotenv

load_dotenv()
pymysql.install_as_MySQLdb()

# Create the SQLAlchemy engine
engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))

# Connect to the database
# with engine.connect() as conn:
#
#         result = conn.execute(text("SELECT * FROM jobs"))
#         #
#         # # Fetch all results
#         # result_all = result.fetchall()
#         #
#         # # Print results
#         # print("Result All:", result_all)
#         #
#         # # Get column names
#         # column_names = result.keys()
#         #
#         # # Convert the first row (tuple) to a dictionary
#         # first_element = result_all[0]
#         # first_result_dict = dict(zip(column_names, first_element))
#         #
#         # print("Type(result_all):", type(result_all))
#         # print("Type(first_element):", type(first_element))
#         # print("Type(first_result_dict):", type(first_result_dict))
#         # print("First Result Dictionary:", first_result_dict)
#         column_names=result.keys()
#         result_dicts=[]
#         for row  in result.fetchall():
#             result_dicts.append(dict(zip(column_names, row)))
#         print(result_dicts)
def load_job_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        column_names = result.keys()
        jobs = []
        for row in result.fetchall():
            jobs.append(dict(zip(column_names, row)))
        return jobs

def load_job_from_id(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"),{"val" :  id})
        column_names = result.keys()
        rows= result.fetchall()
        if len(rows) == 0:
            return None
        else:

            return  [dict(zip(column_names, row)) for row in rows]


def add_application_db(job_id, data):
    sql = text("""
        INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
        VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
    """)

    try:
        with engine.connect() as conn:
            result = conn.execute(sql, {
                'job_id': job_id,
                'full_name': data.get('Full_Name'),
                'email': data.get('Email'),
                'linkedin_url': data.get('LinkedIn_URL'),
                'education': data.get('education', ''),  # Default to empty string if not provided
                'work_experience': data.get('work_experience', ''),  # Default to empty string if not provided
                'resume_url': data.get('resume_url', '')  # Default to empty string if not provided
            })
            print("Insert successful:", result.rowcount)
    except SQLAlchemyError as e:
        print(f"Error inserting data: {e}")

