import tweepy
 
def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
 
    auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
    auth.set_access_token(access_token,       access_token_secret)
 
    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return  api
 
 
 
def post_tweets():
 
    consumer_key	   =   '4txB3h76nfwtRwAYqeHezwVwl'
    consumer_secret	   =   'mwmzooPVaEilm7UHJONOYmShaGFQynQ8QnENzUJVF32xf8oSG2'
    access_token	   =   '966151311212367873-LZ6FX7GQPTbB8EdPfzRw4aGsX79eBqS'
    access_token_secret=   'kzGY3RyaomAaVStiNLyttKqMSWEVtoKwBqImBDMh3c4HS'
 
    message = "Hello have a beautiful day"
 
    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret )
 
    ret = api.update_status(status=message)
 
 
if __name__ == '__main__':
    post_tweets()
