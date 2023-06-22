import os

from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    os.getenv("DB_CONNECTION_STRING"),
    connect_args={
        "ssl": {
            "ssl_cert": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("select * from locations"))
    print(result.all())

def load_locations_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from locations"))
        column_names = result.keys()
        jobs = []
        for row in result.all():
            jobs.append(dict(zip(column_names, row)))
        return jobs
    
def load_location_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
       text(f"SELECT * FROM locations WHERE id={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return row

