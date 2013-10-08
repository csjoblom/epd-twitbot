from twitter import Twitter
from default_settings import OAUTH_SECRET, OAUTH_TOKEN, CONSUMER_SECRET, CONSUMER_KEY

def twittercast(occurance):
    """Creates the message from the occurance and tweets it"""

    t = Twitter(auth=OAuth(
            OAUTH_TOKEN,OAUTH_SECRET,
            CONSUMER_KEY,CONSUMER_SECRET))



    tweet = "Incident:%s, %s, %s, %s" % (occurance['ID'], occurance['Description'], occurance['TimeReceived'], occurance['Location'])
    print tweet
    try:
        t.statuses.update(status="%" % tweet)
    except:
        print "Unable to post to twitter."
