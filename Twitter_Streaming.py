import twitter

APP_KEY = ''  #CONSUMER KEY
APP_SECRET = ''  #CONSUMER SECRET
OAUTH_TOKEN = ''  #ACCESS TOKEN 
OAUTH_TOKEN_SECRET = ''  #ACCESS TOKEN SECRET

auth = twitter.OAuth(
    consumer_key=APP_KEY,
    consumer_secret=APP_SECRET,
    token=OAUTH_TOKEN,
    token_secret=OAUTH_TOKEN_SECRET
)

stream = twitter.stream.TwitterStream(auth=auth, domain='userstream.twitter.com')

for msg in stream.user():
    if 'direct_message' in msg:
        print msg['direct_message']['text']