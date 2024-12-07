from flask import Flask
import redis
import os

app = Flask(__name__)
redis_client = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    visits = redis_client.incr('visits')
    return f'Hello! Number of visits: {visits}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500)