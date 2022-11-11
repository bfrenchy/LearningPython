import tweepy # using 3.8
import time

consumer_key = 'string'
consumer_secret = 'string'
access_token = 'string'
access_token_secret = 'string'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def limit_handle(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300) # wait 300ms

# auto-follow back
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	if follower.name == 'ben_c_french': # that's my handle!
		follower.follow()
		break

# retweet my own mentions
search_string = 'python'
numberOfTweets = 2

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numberOfTweets)):
	try:
		tweet.favorite()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break