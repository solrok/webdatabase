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
            jobs = [dict(zip(column_names, row)) for row in rows]
            return  jobs


