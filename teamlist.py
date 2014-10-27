#####################################################
#
# A library for getting team lists out of the Blue Alliance API
#
# Authors: Andrew Merrill and Jacob Bendicksen (Fall 2014)
#
# Requires the blueapi.py library
######################################################

import blueapi

#returns a list of all the teams currently competing in FRC
def getTeamList():
    teamList = []
    for n in (0,10):
        teamList.extend(blueapi.getTeams(n))
    return teamList
