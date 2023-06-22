from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://ntes6nmglk8xd0izmde6:pscale_pw_uOCa84U06Hz6KuUbo0YZPtMARnduiYyuUaY0wGVk7Et@aws.connect.psdb.cloud/saratoga-public-restrooms?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
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
