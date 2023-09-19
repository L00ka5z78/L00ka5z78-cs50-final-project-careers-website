from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://g676u90rbk5cu76gon38:pscale_pw_uLlW7yDthDtmrrLyJYzuobRl8cprzzsADRRaMDOgsno@aws.connect.psdb.cloud/careers?charset=utf8mb4"
)

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
