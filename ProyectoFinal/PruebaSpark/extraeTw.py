
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'lcdKl61g4o20ToBuqDHeGWIh5'
csecret = 'izaJyIBclqK5XdPb7wtt4K7pvoa5o0zQhNBP58RqQFBNIpsgx0'
atoken = '26922451-I50wrMPKRPhBs59XQBH1CvaTtltQfcmr130ZmrTCm'
asecret = 'XmkriM5kHpV4572ziLP2lkmpMVS1RAkX0Xah8GTltm72A'

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
