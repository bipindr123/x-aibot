import tweepy
from dotenv import load_dotenv
import os

load_dotenv("./.env")
bearer_token = os.getenv("X_API_KEY")
print(bearer_token)

# Authenticate to Twitter
client = tweepy.Client(bearer_token)
us = client.get_me()
print(us)