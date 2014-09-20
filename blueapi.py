#####################################################
#
# A library for accessing the Blue Alliance API
#
# Authors: Andrew Merrill and Jacob Bendicksen (Fall 2014)
#
######################################################

import urllib
import urllib2
import json

# given the trailing part of an api request,
#  returns a dictionary of data
# example selector: 'team/frc1540'

def sendAPIRequest(selector):
    api_server = "www.thebluealliance.com"
    api_base_url = '/api/v2/'
    full_url = 'http://' + api_server + api_base_url + selector
    headers = dict()
    headers['X-TBA-App-Id'] = 'frcyyyy:your_app:v1' #replace this with something that describes you/your team
    print 'URL:', full_url
    request = urllib2.Request(full_url, None, headers)
    connection = urllib2.urlopen(request)
    code = connection.getcode()
    if code == 200:
        data = connection.read()
        datadict = json.loads(data)
        return datadict
    else:
        raise Exception('blue alliance returned code: ' + str(code))


#given a team number,
# returns data about that team
def getTeamInfo(teamNumber):
  return sendAPIRequest('team/frc' + str(teamNumber))

#given a team number and year,
# returns data for how that team did at all events that year
def getTeamYearInfo(teamNumber, year):
  return sendAPIRequest('team/frc'+str(teamNumber)+'/'+str(year)+'/events')

#given a page number,
# returns a list of teams starting at 500*number and ending at 499+number
#this returns a massive block of text!!!
def getTeams(pageNumber):
  return sendAPIRequest('teams/' + str(pageNumber))

#given a team number and event key,
# returns the award(s) won by the team at the event
def getTeamEventAwards(teamNumber, eventKey):
  return sendAPIRequest('team/frc' + str(teamNumber) + '/event/' + str(eventKey) + '/awards')

#given a team number and event key,
# returns the team's matches from that event
def getTeamEventMatches(teamNumber, eventKey):
  return sendAPIRequest('team/frc' + str(teamNumber) + '/event/' + str(eventKey) + '/matches')

#given a team number,
# returns a list of years participated in FRC
def getTeamYearsParticipated(teamNumber):
  return sendAPIRequest('team/frc' + str(teamNumber) + '/years_participated')

#given a team number and year,
# returns links to robot photos/videos from that year (depending on what they've posted)
def getTeamMedia(teamNumber, year):
  return sendAPIRequest('team/frc' + str(teamNumber) + '/' + str(year) + '/media')

#given a year,
# returns a whole lotta data for that year's events (I'll figure out what it is later)
def getEventList(year):
  return sendAPIRequest('events/' + str(year))

#given an event key,
# returns a list of teams attending with all of their data
def getEventTeams(eventKey):
  return sendAPIRequest('event/' + str(eventKey) + '/teams')

#given an event key,
# returns a list of all matches and their results
def getEventMatches(eventKey):
  return sendAPIRequest('event/' + str(eventKey) + '/matches')

#given an event key,
# returns a list of calculated stats (OPR, CCWM, DPR)
def getEventStats(eventKey):
  return sendAPIRequest('event/' + str(eventKey) + '/stats')

#given an event key,
# returns the final rankings with key stats
def getEventRankings(eventKey):
  return sendAPIRequest('event/' + str(eventKey) + '/rankings')

#given an event key,
# returns the awards won at that event and which teams won them
def getEventAwards(eventKey):
  return sendAPIRequest('event/' + str(eventKey) + '/awards')

#given an event key,
# returns the district/qualification points gained at that event
def getEventDistrictPoints(eventKey):
  return sendAPIRequest('event/' + str(eventKey) + '/district_points')

#given a year,
# returns which districts existed that year (i.e. fim, pnw, ne, mar)
def getDistrictList(year):
  return sendAPIRequest('districts/' + str(year))

#given a district area and year,
# returns all district events (including district championship), results, and elimination alliances
def getDistrictEvents(districtArea, year):
  return sendAPIRequest('district/' + str(districtArea) + '/' + str(year) + '/events')

#given a district area and year,
# returns rankings and event breakdowns for each team
def getDistrictRankings(districtArea, year):
  return sendAPIRequest('district/' + str(districtArea) + '/' + str(year) + '/rankings')
