from twitter import *
from default_settings import OAUTH_SECRET, OAUTH_TOKEN, CONSUMER_SECRET, CONSUMER_KEY

def twittercast(occurance):
    """Creates the message from the occurance and tweets it"""

    t = Twitter(auth=OAuth(
            OAUTH_TOKEN,OAUTH_SECRET,
            CONSUMER_KEY,CONSUMER_SECRET))
    description = str(occurance['Description'])

    tweet = "#%s, %s, %s, Incident ID:%s" % (description.replace(" ", "").lower(), occurance['TimeReceived'], occurance['Location'], occurance['ID'])
    print tweet
    try:
        t.statuses.update(status="%s" % tweet)
    except:
        print "Unable to post to twitter."
