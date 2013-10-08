import sqlite3
import nabber
from dbhandler import db_session, init_db
from models import Incident




def create_db():
    """Creates a sqlite3 database using our models"""
    db_session()
    init_db()
    db_session.remove()

def addto_db():
    """adds our incidents to the db"""
    db_session()
    crimelist = nabber.epdcrimelist()
    for each in crimelist:
        #create new Incident instance
        incident = Incident(id = each['ID'],
                            poresp = each['PoResp'],
                            description = each['Description'],
                            ofc = each['OFC'],
                            timerec = each['TimeReceived'],
                            location = each['Location'],
                            eventNum = each['EventNum'],
                            priority = each['Priority'],
                            caseNo = each['CaseNo'])

        #add to the database and then commit the changes.
        try:
            db_session.add(incident)
            db_session.commit()
        except:
            print "Record Exists." #we discard the record since it probably exists

    db_session.remove()

if __name__ == "__main__":
    addto_db()
