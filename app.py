from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis-service', port=6379, db=0, decode_responses=True)

def get_greetings_from_redis():
    cached_greeting = redis_client.get('latest_greeting')
    if cached_greeting:
        return cached_greeting
    else:
        # If the greeting is not cached in Redis, fetch it and cache it
        greeting = "Welcome to CI/CD + Docker Course!"
        redis_client.set('latest_greeting', greeting)
        return greeting

@app.route('/greetings')
def greetings():
    greeting = get_greetings_from_redis()
    return greeting

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=3000)