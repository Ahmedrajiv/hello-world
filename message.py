import tweepy
def get_api(cfg):
 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)
 
api.update_status(status="This is a tweet sent automatically by a Python script! Dont worry, friends. Im just sending")
