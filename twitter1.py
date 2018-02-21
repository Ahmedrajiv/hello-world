import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "4txB3h76nfwtRwAYqeHezwVwl",
    "consumer_secret"     : "mwmzooPVaEilm7UHJONOYmShaGFQynQ8QnENzUJVF32xf8oSG2",
    "access_token"        : "966151311212367873-LZ6FX7GQPTbB8EdPfzRw4aGsX79eBqS",
    "access_token_secret" : "kzGY3RyaomAaVStiNLyttKqMSWEVtoKwBqImBDMh3c4HS",
    }

  api = get_api(cfg)
  tweet = "Hello Rajiv Uddin Ahmed"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
