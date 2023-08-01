import os

from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from datetime import date

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
        locations = []
        for row in result.all():
            locations.append(dict(zip(column_names, row)))
        return locations

def load_comments_from_db():
   with engine.connect() as conn:
      result = conn.execute(text("select * from comments"))
      column_names = result.keys()
      comments = []
      for row in result.all():
         comments.append(dict(zip(column_names, row)))
      return comments

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

def add_location_to_db(data):
   row = {
      "location_name": data["location_name"],
      "address": data["address"],
      "open_hours": data["open_hours"],
      "additional_info": data["additional_info"]
   }
   with engine.connect() as conn:
      query = text("INSERT INTO newLocations (location_name, address, open_hours, additional_info) VALUES (:location_name, :address, :open_hours, :additional_info)")
      conn.execute(query, row)

def add_comment_to_db(location_id, data):
   row = {
      "location_id": location_id,
      "user_name": data["user_name"],
      "post_date": date,
      "rating": data["rating"],
      "user_comment": data["comment"]
   }
   with engine.connect() as conn:
      query = text("INSERT INTO comments (location_id, user_name, post_date, rating, user_comment) VALUES (:location_id, :user_name, curdate(), :rating, :user_comment)")
      conn.execute(query, row)

def get_location_rating(id):
   with engine.connect() as conn:
    result = conn.execute(
       text(f"SELECT rating FROM comments WHERE location_id={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row.rating)
    if len(rows) == 0:
      return None
    else:
      return average_rows(rows)
    
def average_rows(rows):
   x = 0
   for row in rows:
      x += row
   average = x / len(rows)
   return average

def update_rating_in_db(id, rating):
   with engine.connect() as conn:
      query = text(f" UPDATE locations SET rating = {rating} WHERE id={id}")
      conn.execute(query)