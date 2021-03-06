Eugene Police Data Twitter Bot
=====================================

Runs @epdcast on twitter https://www.twitter.com/epdcast

Created by:

*   Chris Sjoblom
*   chris.sjoblom@gmail.com
*   Eugene, Oregon

The purpose of this bot is to collect public data from the EPD and publish it to twitter. Information will also be stored in a database for later mapping/data analysis.

Current Status
--------------

Main webcrawler and twitter status update functions now have basic functionality. Project runs great with cron and automation seems to be working correctly. Will collect data for the next couple weeks and then figure out something to do with it all.

Dependencies
------------
*   python/pip - it's all python, pip is needed to install requirements
*   virtualenv - not required but highly recommended
*   lxml - for html crawling/data grabbing. (If you can't install lxml on ubuntu/debian please be sure to apt-get libxml2-dev and libxslt-dev and attempt to install again using pip)
*   sqlalchemy - for database interaction. (currently configured for sqlite3)
*   twitter - python twitter API interaction
*   pygeocoder - grabs latitude/longitude based on an address (for use with google maps)

You can install requirements automatically within a virtualenv by using pip install -r requirements.txt in the base directory of this project.

File Structure
--------------

*   dbhandler.py - handles sqlalchemy configuration, here you can switch between different database types/configurations.
*   default_settings.py - handles twitter OAuth and Consumer settings.
*   epdtwitter.py - contains two functions - create_db() and add_incident(). this will most likely be the job that runs every 10 minutes to check for updates/post to twitter.
*   nabber.py - uses lxml to crawl through the EPD website, targets the table and pulls all of the data into a list of dictionaries.
*   models.py - contains metadata information for our database, modify if you need to add/change database schema stuff.
*   twittercast.py - contains twittercast function that updates twitter status for each new instance/occurance.

Disclaimer: This is a hobby project. It may or may not be under active development at any given point. If you have any questions or if I'm doing something terrible please feel free to shoot me an email.
