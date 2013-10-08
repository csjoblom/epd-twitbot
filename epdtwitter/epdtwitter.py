import sqlite3
import nabber
from dbhandler import db_session, init_db
from models import Incident
from sqlalchemy import exc

def create_db():
    """Creates a sqlite3 database using our models"""
    db_session()
    init_db()
    db_session.remove()

def add_incident():
    """adds our incidents to the db"""

    incidentlist = nabber.epdcrimelist()
    for occurance in incidentlist:
        db_session()
        #create new Incident instance
        incident = Incident(id = occurance['ID'],
                            poresp = occurance['PoResp'],
                            description = occurance['Description'],
                            ofc = occurance['OFC'],
                            timerec = occurance['TimeReceived'],
                            location = occurance['Location'],
                            eventNum = occurance['EventNum'],
                            priority = occurance['Priority'],
                            caseNo = occurance['CaseNo'])

        db_session.add(incident)

        #add to the database and then commit the changes.
        try:
            db_session.commit()
            print "Record %s Added." % (occurance['ID'])

        except exc.SQLAlchemyError:
           print "Record %s Exists." % (occurance['ID'])#we discard the record since it probably existsa
           pass

        db_session.remove()

if __name__ == "__main__":
    create_db()
    add_incident()
