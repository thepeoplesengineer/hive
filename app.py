from flask import Flask, request
from bot.twitter_bot import TwitterBot

# Initialize Flask app
app = Flask(__name__)

# Initialize the Twitter bot
twitter_bot = TwitterBot()

@app.route('/')
def home():
    return "Twitter Bot is running!"

@app.route('/tweet', methods=['POST'])
def post_tweet():
    """Endpoint to post a tweet."""
    data = request.json
    message = data.get("message")
    if not message:
        return {"error": "Message is required"}, 400
    response = twitter_bot.tweet(message)
    return {"response": response}

@app.route('/tweets/<username>', methods=['GET'])
def get_tweets(username):
    """Endpoint to fetch a user's latest tweets."""
    max_results = request.args.get("max_results", 10)
    try:
        max_results = int(max_results)
    except ValueError:
        return {"error": "max_results must be an integer"}, 400
    response = twitter_bot.get_user_tweets(username=username, max_results=max_results)
    return {"tweets": response}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
