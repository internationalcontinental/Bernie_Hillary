import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

        #Variables that contains the user credentials to access Twitter API 
atoken = "719527275834818561-5hY4KfOhczFYeXA73fn6rDQ0yqSSb6k"
asecret = "37Nd9vWGumY0RukEOaid6H7eAwpHJsWPy86m4G0MS3AGI"
ckey = "bWbdkXRfCtn61tWKgAJPzXMJu"
csecret = "w3bJirguKsOtAmoOzjnySvucLSzerTo1zMTXDkExOU7HqpDfsD"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
 

 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('primaryNY1.txt', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#feelthebern','#hillaryforameica','#bernie2016','#hillary2016','Sanders','Clinton'])



 
