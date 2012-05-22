#!/usr/bin/env python
# 
#  profilemapper.py
#  vatdata
#  
#  Created by James Scott on 2012-05-21.
# 

def profileMapper(clientList):
    """maps the split list to a dictionary for teh columns"""
    dataDict = {}

    dataDict['callsign'] = clientList[0]
    dataDict['cid'] = clientList[1]
    dataDict['realname'] = clientList[2]
    dataDict['clienttype'] = clientList[3]
    dataDict['frequency'] = clientList[4]
    dataDict['latitude'] = clientList[5]
    dataDict['longitude'] = clientList[6]
    dataDict['altitude'] = clientList[7]
    dataDict['groundspeed'] = clientList[8]
    dataDict['planned_aircraft'] = clientList[9]
    dataDict['planned_tascruise'] = clientList[10]
    dataDict['planned_depairport'] = clientList[11]
    dataDict['planned_altitude'] = clientList[12]
    dataDict['planned_destairport'] = clientList[13]
    dataDict['server'] = clientList[14]
    dataDict['protrevision'] = clientList[15]
    dataDict['rating'] = clientList[16]
    dataDict['transponder'] = clientList[17]
    dataDict['facilitytype'] = clientList[18]
    dataDict['visualrange'] = clientList[19]
    dataDict['planned_revision'] = clientList[20]
    dataDict['planned_flighttype'] = clientList[21]
    dataDict['planned_deptime'] = clientList[22]
    dataDict['planned_actdeptime'] = clientList[23]
    dataDict['planned_hrsenroute'] = clientList[24]
    dataDict['planned_minenroute'] = clientList[25]
    dataDict['planned_hrsfuel'] = clientList[26]
    dataDict['planned_minfuel'] = clientList[27]
    dataDict['planned_altairport'] = clientList[28]
    dataDict['planned_remarks'] = clientList[29]
    dataDict['planned_route'] = clientList[30]
    dataDict['planned_depairport_lat'] = clientList[31]
    dataDict['planned_depairport_lon'] = clientList[32]
    dataDict['planned_destairport_lat'] = clientList[33]
    dataDict['planned_destairport_lon'] = clientList[34]
    dataDict['atis_message'] = clientList[35]
    dataDict['time_last_atis_received'] = clientList[36]
    dataDict['time_logon'] = clientList[37]
    dataDict['heading'] = clientList[38]
    dataDict['QNH_iHg'] = clientList[39]
    dataDict['QNH_Mb'] = clientList[40]
    return dataDict