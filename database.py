from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://g676u90rbk5cu76gon38:pscale_pw_uLlW7yDthDtmrrLyJYzuobRl8cprzzsADRRaMDOgsno@aws.connect.psdb.cloud/careers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/ca.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
