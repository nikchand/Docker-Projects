# app/app.py
from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (service name is 'redis')
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello():
    count = r.incr('hits')  # Increment counter
    return f'Hello! This page has been visited {count} times.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
