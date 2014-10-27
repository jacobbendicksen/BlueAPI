import blueapi, teaminfo

def getCMPTeams():
    cmpteams = []
    allcmpteams = []
    cmpteams.extend(blueapi.getEventTeams('2014cur'))
    cmpteams.extend(blueapi.getEventTeams('2014arc'))
    cmpteams.extend(blueapi.getEventTeams('2014new'))
    cmpteams.extend(blueapi.getEventTeams('2014gal'))
    for team in cmpteams:
        allcmpteams.append(team['team_number'])
    allcmpteams.sort()
    return allcmpteams

def getChairmansTeams():
    chairmansteams = []
    for team in getCMPTeams():
        print "Processing team", team
        events = blueapi.getTeamYearInfo(team, 2014)
        for event in events:
            awards = blueapi.getTeamEventAwards(team,event['key'])
            for n in awards:
                if n['name'] == "Regional Chairman\'s Award":
                    chairmansteams.append(team)
                    print "Chairman's teams:", chairmansteams
                    break
            else:
                pass
                #print "Awards:", awards
    return chairmansteams

print "CMP teams:", getCMPTeams()
print getChairmansTeams()

for team in getChairmansTeams:
    print team, teaminfo.teamWebsite(team)
