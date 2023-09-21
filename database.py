from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ['DB_CONNECTION_STRING']
# db_connection_string = "mysql+pymysql://gazqn9tgfbtv60bmtiao:pscale_pw_GDtxRV1WOomRqwWqqQNRLOYkSUyHPjiCgjZEs8wKZCU@aws.connect.psdb.cloud/careers?charset=utf8mb4"
# db_connection_string = "mysql+pymysql://2a9gyc7yrqtbzsfmj854:pscale_pw_B9P9oKlxEn1DULWztsWEQBO3TVV7EFUINxOeGYBq9bh@aws.connect.psdb.cloud/careers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []

    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
