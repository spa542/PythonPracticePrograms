import tweepy # twitter api
import time # time function

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Online when accepted
auth.set_access_token(access_token, access_token_secret) # Online when accepted

api = tweepy.API(auth)
user = api.me()

print(user.followers_count)

def limit_handle(cursor):
    try:
        while True:
            yield cursor.next
    except: tweepy.RateLimitError:
        time.sleep(1000)


# Generous Bot that follows back
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    follower.follow()

# Narcisistic Bot
searchString = 'python'
numberOfTweets = 2

for tweet in limit_handle(tweepy.Cursor(api.search, searchString).items(numberOfTweets)):
    try:
        tweet.retweet()
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
