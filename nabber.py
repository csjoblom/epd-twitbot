import lxml.html
import lxml.etree
import urllib2

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
		datarow = str(each.text_content())
		if datarow == "":
			pass
			#print "\nNew Report"
		else:
			#print ("Line: %s") % datarow
			if datarow.startswith("Police Response:"):
				incidentDict = {}
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
				incidentDict['TimeReceived'] = datarow[9:]
			elif datarow.startswith("Disp:"):
				incidentDict['Disp'] = datarow[6:]
			elif datarow.startswith("Location:"):
				incidentDict['Location'] = datarow[9:]
			elif datarow.startswith("Event Number:"):
				incidentDict["EventNum"] = datarow[13:]
			elif datarow.startswith("ID:"):
				incidentDict['ID'] = datarow[4:]
			elif datarow.startswith("Priority:"):
				incidentDict['Priority'] = datarow[9:]
			elif datarow.startswith("Case No:"):
				incidentDict['CaseNo'] = datarow[8:]
				resultlist.append(incidentDict)
	return resultlist