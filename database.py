from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
# db_connection_string = "mysql+pymysql://gazqn9tgfbtv60bmtiao:pscale_pw_GDtxRV1WOomRqwWqqQNRLOYkSUyHPjiCgjZEs8wKZCU@aws.connect.psdb.cloud/careers?charset=utf8mb4"
#dzialajacy ponizej
# db_connection_string = "mysql+pymysql://q4mig5l1r9wfn3skmv01:pscale_pw_JY6951p04eG1fCB7iA7Q48wIfYU9CaIFIOThDPwDqkN@aws.connect.psdb.cloud/careers?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
            # "ca": "/etc/ssl/certs/ca-certificates.crt"
        }
    })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []

    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs


# def load_job_from_db(id):
#   with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), val=id)
#     rows = result.all()
#     if len(rows) == 0:
#       return None
#     else:
#       return dict(rows[0])


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}"))
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return [dict(row) for row in rows]


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
        "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )

    conn.execute(query,
                 job_id=job_id,
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])
