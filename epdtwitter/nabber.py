import lxml.html
import lxml.etree
import urllib2
import sqlite3
from datetime import datetime

def epdcrimelist():
    """Grabs latest police activity online and stores it in a list of dictionaries"""
    opener = urllib2.build_opener()
    opener.addheaders=[('User-agent', 'Mozilla/5.0')]
    infile = opener.open('http://ceapps.eugene-or.gov/epdpubliccad/')
    html = infile.read()
    doc = lxml.html.document_fromstring(html)
    opener.close()
    result = doc.xpath('/html/body/form/div[2]/table[2]/tr/td')
    resultlist = []
    for each in result:
        #print each.text_content().decode('UTF-8').encode('ascii','xmlcharrefreplace')
        datarow = each.text_content()
        if datarow == "":
            pass
            #print "\nNew Report"
        else:
            #print ("Line: %s") % datarow
            if datarow.startswith("Police Response:"):
                incidentDict = {}
                incidentDict['Location'] = ""
                if len(datarow) > 17:
                    incidentDict['PoResp'] = datarow[17:]
                else:
                    incidentDict['PoResp'] = ""
            elif datarow.startswith("Incident Desc:"):
                incidentDict['Description'] = datarow[15:]
            elif datarow.startswith("OFC:"):
                if len(datarow) > 5:
                    incidentDict['OFC'] = datarow[5:]
                else:
                    incidentDict['OFC'] = ""
            elif datarow.startswith("Received:"):
                date_object = datetime.strptime(str(datarow[10:]), '%m/%d/%Y %I:%M:%S %p')
                incidentDict['TimeReceived'] = date_object
            elif datarow.startswith("Disp:"):
                incidentDict['Disp'] = datarow[6:]
            elif datarow.startswith("Location:"):
                incidentDict['Location'] = datarow[10:]
            elif datarow.startswith("Event Number:"):
                incidentDict["EventNum"] = datarow[14:]
            elif datarow.startswith("ID:"):
                incidentDict['ID'] = datarow[4:]
            elif datarow.startswith("Priority:"):
                incidentDict['Priority'] = datarow[10:]
            elif datarow.startswith("Case No:"):
                incidentDict['CaseNo'] = datarow[9:]
                resultlist.append(incidentDict)
    return resultlist

if __name__ == "__main__":
   q =  epdcrimelist()
   for each in q:
       print each
