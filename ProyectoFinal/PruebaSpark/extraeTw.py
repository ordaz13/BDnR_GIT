
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = ''
csecret = ''
atoken = ''
asecret = ''

class listener(StreamListener):
    def on_data(self,data):
        print(data)
        return True
    def on_error(self,status):
        print(status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

twitterStream.filter(track=["Guadalupe"])
