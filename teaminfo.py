#####################################################
#
# A library for getting team information out of the Blue Alliance API
#
# Authors: Andrew Merrill and Jacob Bendicksen (Fall 2014)
#
# Requires the blueapi.py library
######################################################

import blueapi

teamNumber=raw_input("Team number: \n")

teamInfo=blueapi.getTeamInfo(teamNumber)
teamWebsite=teamInfo['website'] #www.team1540.org
teamName=teamInfo['name'] #Catlin Gabel High School
teamLocality=teamInfo['locality'] #Portland
teamNickname=teamInfo['nickname'] #The Flaming Chickens
teamRegion=teamInfo['region'] #OR
teamLocation=teamInfo['location'] #Portland, OR, USA
teamNumber=teamInfo['team_number'] #1540
teamKey=teamInfo['key'] #frc1540
teamCountry=teamInfo['country_name'] #USA
teamRookieYear=teamInfo['rookie_year'] #2005
