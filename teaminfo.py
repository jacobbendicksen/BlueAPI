#####################################################
#
# A library for getting team information out of the Blue Alliance API
#
# Authors: Andrew Merrill and Jacob Bendicksen (Fall 2014)
#
# Requires the blueapi.py library
######################################################

import blueapi

#returns the team's website
def teamWebsite(teamNumber):
    return blueapi.getTeamInfo(teamNumber)['website']

#returns the team's name
def teamName(teamNumber):
    return blueapi.getTeamInfo(teamNumber)['name']

#returns the team's city
def teamCity(teamNumber):
    return blueapi.getTeamInfo(teamNumber)['locality']

#returns the team's nickname
def teamNickname(teamNumber):
    return blueapi.getTeamInfo(teamNumber)['nickname']

#returns the team's region (usually state)
def teamRegion(teamNumber):
    return blueapi.getTeamInfo(teamNumber)['region']

#returns the team's location
def teamLocation(teamNumber):
    return blueapi.getTeamInfo(teamNumber)['location']

#returns the team's TBA key
def teamKey(teamNumber):
    return blueapi.getTeamInfo(teamNumber)['key']

#returns the team's country
def teamCountry(teamNumber):
    return blueapi.getTeamInfo(teamNumber)['country_name']

#returns the team's rookie year
def teamRookieYear(teamNumber):
    return blueapi.getTeamInfo(teamNumber)['rookie_year']
