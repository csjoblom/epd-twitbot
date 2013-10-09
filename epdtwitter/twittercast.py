from twitter import *
from pygeocoder import Geocoder

from default_settings import OAUTH_SECRET, OAUTH_TOKEN, CONSUMER_SECRET, CONSUMER_KEY

def geolocale(address):
    """Gets Lat/Longitude for any given address"""
    results = Geocoder.geocode(address)
    return results[0].coordinates

def twittercast(occurance):
    """Creates the message from the occurance and tweets it"""

    t = Twitter(auth=OAuth(
            OAUTH_TOKEN,OAUTH_SECRET,
            CONSUMER_KEY,CONSUMER_SECRET))
    description = str(occurance['Description'])
    locale = geolocale(occurance['Location'])
    maplink = "https://maps.google.com/?q=%s,%s" % (locale[0],locale[1])

    tweet = "#%s, %s, %s, %s , ID:%s" % (description.replace(" ", "").lower().replace("(s)", "s").replace("&", "and"), occurance['TimeReceived'], occurance['Location'], maplink, occurance['ID'])
    print tweet
    try:
        t.statuses.update(status="%s" % tweet)
    except:
        print "Unable to post to twitter."
