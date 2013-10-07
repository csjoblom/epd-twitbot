import datetime
from sqlalchemy import Column, Integer, String, DateTime
from dbhandler import Base

class Incident(Base):
    """Incident Model"""
    __tablename__ = 'incident'
    id = Column(Integer, primary_key=True)
    poresp = Column(String(50))
    description = Column(String(100))
    ofc = Column(String(100))
    timerec = Column(DateTime(timezone=True))
    location = Column(String(150))
    eventNum = Column(String(50))
    priority = Column(Integer)
    caseNo = Column(String(100))

    def __repr__(self):
        return '<Incident %r>' % (self.id)
