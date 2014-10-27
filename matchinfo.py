#####################################################
#
# A library for getting match information for a given team at a given event
# out of the Blue Alliance API
#
# Authors: Andrew Merrill and Jacob Bendicksen (Fall 2014)
#
# Requires the blueapi.py library
######################################################

#this doesn't currently fully work

import blueapi

teamNumber = 1540
eventKey = '2014orosu'

#returns a list of qualification matches that the team played in
def getTeamQualMatches(teamNumber,eventKey):
    matches = []
    for n in range(0,len(blueapi.getTeamEventMatches(eventKey,teamNumber))):
        if blueapi.getTeamEventMatches(teamNumber,eventKey)[n]['comp_level'] == 'qm':
            matches.append(blueapi.getTeamEventMatches(eventKey)[n]['match_number'])
    matches.sort()
    return matches

#returns a list of qualification matches that the team played in
def getQualMatches(eventKey):
    matches = []
    for n in range(0,len(blueapi.getEventMatches(eventKey))):
        if blueapi.getEventMatches(eventKey)[n]['comp_level'] == 'qm':
            matches.append(blueapi.getEventMatches(eventKey)[n]['match_number'])
    matches.sort()
    return matches

#returns a list of quarterfinal matches that the team played in
def getTeamQFMatches(teamNumber, eventKey):
    matches = []
    for n in range(0,len(blueapi.getTeamEventMatches(eventKey))):
        if blueapi.getTeamEventMatches(eventKey)[n]['comp_level'] == 'qf':
            matches.append(blueapi.getTeamEventMatches(eventKey)[n]['match_number'])
    matches.sort()
    return matches

#returns a list of quarterfinal matches that the team played in
def getQFMatches(eventKey):
    matches = []
    for n in range(0,len(blueapi.getEventMatches(eventKey))):
        if blueapi.getEventMatches(eventKey)[n]['comp_level'] == 'qf':
            matches.append(blueapi.getEventMatches(eventKey)[n]['match_number'])
    matches.sort()
    return matches

#returns a list of semifinal matches that the team played in
def getTeamSFMatches(teamNumber, eventKey):
    matches = []
    for n in range(0,len(blueapi.getTeamEventMatches(eventKey))):
        if blueapi.getTeamEventMatches(eventKey)[n]['comp_level'] == 'sf':
            matches.append(blueapi.getTeamEventMatches(eventKey)[n]['match_number'])
    matches.sort()
    return matches

#returns a list of semifinal matches that the team played in
def getSFMatches(eventKey):
    matches = []
    for n in range(0,len(blueapi.getEventMatches(eventKey))):
        if blueapi.getEventMatches(eventKey)[n]['comp_level'] == 'sf':
            matches.append(blueapi.getEventMatches(eventKey)[n]['match_number'])
    matches.sort()
    return matches

#returns a list of finals matches that the team played in
def getTeamFMatches(teamNumber, eventKey):
    matches = []
    for n in range(0,len(blueapi.getTeamEventMatches(eventKey))):
        if blueapi.getTeamEventMatches(eventKey)[n]['comp_level'] == 'f':
            matches.append(blueapi.getTeamEventMatches(eventKey)[n]['match_number'])
    matches.sort()
    return matches

#returns a list of qualification matches that the team played in
def getFMatches(eventKey):
    matches = []
    for n in range(0,len(blueapi.getEventMatches(eventKey))):
        if blueapi.getEventMatches(eventKey)[n]['comp_level'] == 'f':
            matches.append(blueapi.getEventMatches(eventKey)[n]['match_number'])
    matches.sort()
    return matches

def matchRedScore(matchNumber,eventKey):
    return blueapi.getEventMatches(eventKey)[matchNumber]['alliances']['red']['score']

def matchBlueScore(matchNumber,eventKey):
    return blueapi.getEventMatches(eventKey)[matchNumber]['alliances']['blue']['teams']

def matchRedTeams(matchNumber,eventKey):
    return blueapi.getEventMatches(eventKey)[matchNumber]['alliances']['red']['teams']

def matchBlueTeams(matchNumber,eventKey):
    return blueapi.getEventMatches(eventKey)[matchNumber]['alliances']['blue']['teams']


#  matchVideo = match_list[match]['videos']
#  setNumber = match_list[match]['set_number']
#  timeString = match_list[match]['time_string']
#  matchKey = match_list[match]['key']
#  matchTime = match_list[match]['time']
#  scoreBreakdown = match_list[match]['score_breakdown']
#  eventKey = match_list[match]['event_key']

print matchRedTeams(24,'2014orosu')
