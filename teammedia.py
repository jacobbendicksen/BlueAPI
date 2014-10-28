#####################################################
#
# A library for accessing FRC team media via the Blue Alliance API
#
# Authors: Andrew Merrill and Jacob Bendicksen (Fall 2014)
#
######################################################

import blueapi

def getTeamMedia(teamNumber,year):
    mediaList = []
    media = blueapi.getTeamMedia(teamNumber,year)
    for n in range(0,len(media)):
        if media[n]['type'] == "cdphotothread":
            mediaList.append("http://www.chiefdelphi.com/media/img/" + media[n]['details']['image_partial'])
        elif media[n]['type'] == "youtube":
            mediaList.append("www.youtube.com/watch?v=" + media[n]['foreign_key'] + "&feature=youtu.be")
    return mediaList

print getTeamMedia(254,2014)
