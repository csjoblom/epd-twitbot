Eugene Police Department Twitter Bot
=====================================
Created by:

*   Chris Sjoblom
*   chris.sjoblom@gmail.com
*   Eugene, Oregon

The purpose of this bot is to collect public data from the EPD and publish it to twitter. Information will also be stored in a database for later mapping/data analysis.

Current Status
--------------

Development is ongoing, currently the plan is to use SQLAlchemy to store everything in a database. Right now it's configured for sqlite3 but it's easily changeable within the dbhandler.py file.

Dependencies
------------
*   python/pip - it's all python, pip is needed to install requirements
*   virtualenv - not required but highly recommended
*   lxml - for html crawling/data grabbing.
*   sqlalchemy - for database interaction. (currently configured for sqlite3)
*   bpython(dev only) - used for deving in shell with autocompletion.

You can install requirements automatically within a virtualenv by using pip install -r requirements.txt in the base directory of this project.

File Structure
--------------

*   dbhandler.py - handles sqlalchemy configuration, here you can switch between different database types/configurations.
*   epdtwitter.py - contains two functions - create_db() and addto_db(). this will most likely be the job that runs every 10 minutes to check for updates/post to twitter.
*   nabber.py - uses lxml to crawl through the EPD website, targets the table and pulls all of the data into a list of dictionaries.
*   models.py - contains metadata information for our database, modify if you need to add/change database schema stuff.


Disclaimer: This is a hobby project. It may or may not be under active development at any given point. If you have any questions or if I'm doing something terrible please feel free to shoot me an email.
