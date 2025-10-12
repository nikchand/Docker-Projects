from flask import Flask
import redis
import psycopg2
import os

app = Flask(__name__)

# Redis setup
redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, db=0)

# Postgres setup
pg_host = os.environ.get("POSTGRES_HOST", "postgres")
pg_db = os.environ.get("POSTGRES_DB", "flaskdb")
pg_user = os.environ.get("POSTGRES_USER", "flaskuser")
pg_password = os.environ.get("POSTGRES_PASSWORD", "flaskpass")

conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_password)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, counter INT);")
conn.commit()

@app.route("/")
def index():
    # Redis counter
    count = r.incr("counter")
    # Postgres record
    cur.execute("INSERT INTO visits (counter) VALUES (%s);", (count,))
    conn.commit()
    return f"Hello! Redis counter: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

