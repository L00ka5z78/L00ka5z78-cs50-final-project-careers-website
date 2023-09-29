from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
# db_connection_string = "mysql+pymysql://gazqn9tgfbtv60bmtiao:pscale_pw_GDtxRV1WOomRqwWqqQNRLOYkSUyHPjiCgjZEs8wKZCU@aws.connect.psdb.cloud/careers?charset=utf8mb4"
#dzialajacy ponizej
# db_connection_string = "mysql+pymysql://iehz5rumwzvtb0hbboer:pscale_pw_JaDweneV0QzPKqq3A0UYwhMb15qyucK6nkeF2fPwMTX@aws.connect.psdb.cloud/careers?charset=utf8mb4"

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
