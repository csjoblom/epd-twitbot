Eugene Police Department Twitter Bot
=====================================
Created by:

*   Chris Sjoblom
*   chris.sjoblom@gmail.com
*   Eugene, Oregon

The purpose of this bot is to collect public data from the EPD and publish it to twitter. Information will also be stored in a database for later mapping/data analysis.

Current Status
--------------

Main webcrawler and twitter status update functions now have basic functionality. Project runs great with cron and automation seems to be working correctly. I'd like to integrate Latitude/Longitude in tweets and link back to a django generated page containing all information + a map. I would also like to look into using the database information as trend data for map hotspots.

Dependencies
------------
*   python/pip - it's all python, pip is needed to install requirements
*   virtualenv - not required but highly recommended
*   lxml - for html crawling/data grabbing.
*   sqlalchemy - for database interaction. (currently configured for sqlite3)
*   bpython(dev only) - used for deving in shell with autocompletion.
*   twitter - python twitter API interaction

You can install requirements automatically within a virtualenv by using pip install -r requirements.txt in the base directory of this project.

File Structure
--------------

*   dbhandler.py - handles sqlalchemy configuration, here you can switch between different database types/configurations.
*   default_settings.py - handles twitter OAuth and Consumer settings.
*   epdtwitter.py - contains two functions - create_db() and addto_db(). this will most likely be the job that runs every 10 minutes to check for updates/post to twitter.
*   nabber.py - uses lxml to crawl through the EPD website, targets the table and pulls all of the data into a list of dictionaries.
*   models.py - contains metadata information for our database, modify if you need to add/change database schema stuff.
*   twittercast.py - contains twittercast function that updates twitter status for each new instance/occurance.

Disclaimer: This is a hobby project. It may or may not be under active development at any given point. If you have any questions or if I'm doing something terrible please feel free to shoot me an email.
