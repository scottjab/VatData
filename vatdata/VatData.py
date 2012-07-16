#!/usr/bin/env python
# 
#  VatData.py
#  vatdata
#  
#  Created by James Scott on 2012-05-21.
# 


import sys
import os
import requests
import random
import profilemapper
from datetime import datetime, timedelta
import re

class VatData(object):
    """Retrieves and parses the vatsim data file."""
    dataServers     = []
    vatsimServers   = []
    metarServers    = []
    atisServers     = []
    userServers     = []
    vatsimServerListServers = []
    dataList        = []
    dataDicts       = []
    refreshtime     = None
    def __init__(self,server=None):
        self.getDataServers(server)
        self.refreshData()
        
    def parseStatsFile(self,stats):
        """Parses stats file."""
        for line in stats:
            if "url0=" in line:
                line = line[5:]
                self.dataServers.append(line)
            if "url1=" in line:
                line = line[5:]
                self.vatsimServerListServers.append(line)
            if "metar0=" in line:
                line = line[7:]
                self.metarServers.append(line)
            if "atis0=" in line:
                line = line[6:]
                self.atisServers.append(line)
            if "user0=" in line:
                line = line[6:]
                self.userServers.append(line)
        return {'dataServers' : self.dataServers, 'vatsimServerListServers' : self.vatsimServerListServers, 'metarServers' : self.metarServers,'atisServers' : self.atisServers, 'userServers' : self.userServers}    
    
    def getDataServers(self,server):
        """Returns a tuple of data server urls."""

        if server == None:
            server = 'http://status.vatsim.net/status.txt'    
        response = requests.get(server)
        
        
        statsFile = re.split(r'[\n\r]+',response.content)
        return tuple(self.parseStatsFile(statsFile)['dataServers'])
    
    def parseDataFile(self, data):
        """Parses the data file."""
        block = 0
        clientsbool = False
        self.dataDicts = []
        self.dataList = []
        for line in data:
            try:
                if '!CLIENTS:' in line:
                    clientsbool = True
                else:
                    if line.find(';') == 0:
                        if not line.find('; ') == 0:
                            block = block +1
                        if not line.find(';\n') == 0:
                            block = block +1
                        if block > 1:
                            clientsbool = False
                            block = 0
                    if clientsbool:
                        splitline = line.split(u":",40)
                        self.dataList.append(splitline)
                        self.dataDicts.append(profilemapper.profileMapper(splitline))
            except:
                pass
        

    def refreshData(self):
        """Refreshes the data, will not refresh if the data is less than two min old."""
        if self.refreshtime == None:
            #setup an initial value so the file gets refreshed.
            self.refreshtime = datetime.now() - timedelta (hours = 2) 
        if  (datetime.now() - self.refreshtime) > timedelta(minutes = 2):
            #only update the if the data is older than 2 min.
            
            response = requests.Response()
            usedRandomNumber = []
            while response.status_code is not 200:    # If one site fails, try another
                randomServerNumber = random.randint(0, len(self.dataServers) - 1)
                if len(usedRandomNumber) is len(self.dataServers): # Failed too many time, time to die
                    sys.exit(1)
                if randomServerNumber in usedRandomNumber:
                    continue
                response = requests.get(self.dataServers[randomServerNumber])
                usedRandomNumber.append(randomServerNumber)
            unidecoded = unicode(response.content,errors='replace')
            dataFile = re.split(r'[\n\r]+',unidecoded)
            dataFile = [line.replace(u'\xef',u'').replace(u'\ufffd',u'').replace(u'^',u' ') for line in dataFile]
            self.parseDataFile(dataFile)
            #cache the time
            self.refreshtime = datetime.now()
    
    def getDataAsList(self):
        self.refreshData()
        return self.dataList
        
    def getData(self):
        """Returns the list of client Dictionaries."""
        self.refreshData()
        return self.dataDicts
        
def main():
    v = VatData()
    data = v.getData()
    print data
    for user in data:
        if user['clienttype'] == 'ATC' and user['server'] == 'USA-E':
            splitAtis = user['atis_message'].split(" ",2)
            if len(splitAtis) > 2:
                print splitAtis[2]
if __name__ == '__main__':
    main()
