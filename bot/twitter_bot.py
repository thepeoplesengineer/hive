import os
import tweepy
from dotenv import load_dotenv


class TwitterBot:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Twitter API v2 credentials
        self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
        self.consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
        self.consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        self.access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_secret = os.getenv("TWITTER_ACCESS_SECRET")

        # Authenticate with Twitter API v2
        self.client = tweepy.Client(
            bearer_token=self.bearer_token,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_secret,
        )

    def tweet(self, message: str) -> str:
        """Post a tweet using Twitter API v2."""
        try:
            response = self.client.create_tweet(text=message)
            return f"Tweeted successfully! Tweet ID: {response.data['id']}"
        except Exception as e:
            return f"Error tweeting: {str(e)}"

    def get_user_tweets(self, username: str, max_results: int = 10):
        """
        Fetch the latest tweets from a user's timeline using Twitter API v2.
        Note: Converts username to user_id.
        """
        try:
            # Convert username to user_id
            user = self.client.get_user(username=username)
            user_id = user.data.id

            # Fetch tweets
            tweets = self.client.get_users_tweets(id=user_id, max_results=max_results)

            if not tweets.data:
                return "No tweets found."

            return [tweet.text for tweet in tweets.data]
        except Exception as e:
            return f"Error fetching tweets: {str(e)}"

