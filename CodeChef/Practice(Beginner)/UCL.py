# Team
def createNewTeam(teamName):
    team = {'points' : 0, 'goalDifference': 0}
    return team
##################

testCases = int(input())
cases = []

for x in range(testCases):
    teams = {}
    for y in range(12):
        match_details = input()
        match_details = match_details.split('vs.')
        homeTeam = match_details[0].split()
        awayTeam = match_details[1].split()

        ##Get Team Objects
        homeTeamObject = teams.get(homeTeam[0])
        if( homeTeamObject == None ):
            homeTeamObject = createNewTeam(homeTeam[0])
            teams[homeTeam[0]] = homeTeamObject

        awayTeamObject = teams.get(awayTeam[1])
        if( awayTeamObject == None ):
            awayTeamObject = createNewTeam(awayTeam[1])
            teams[awayTeam[1]] = awayTeamObject

        ##Calculate points won
        homeTeamGoals = int(homeTeam[1])
        awayTeamGoals = int(awayTeam[0])

        if(homeTeamGoals > awayTeamGoals):
            homeTeamObject['points'] += 3
        elif(homeTeamGoals < awayTeamGoals):
            awayTeamObject['points'] += 3
        elif(homeTeamGoals == awayTeamGoals):
            awayTeamObject['points'] += 1
            homeTeamObject['points'] += 1

        ##Update Goal Difference
        homeTeamObject['goalDifference'] +=  (homeTeamGoals - awayTeamGoals)
        awayTeamObject['goalDifference'] +=  (awayTeamGoals - homeTeamGoals)

    cases.append(teams)
#Find max two
for case in cases:
    first =  max(case.keys(), key = lambda k: (case[k]["points"], case[k]["difference"]))
    del case[first]
    second = max(case.keys(), key = lambda k: (case[k]["points"], case[k]["difference"]))

    print(first + ' ' + second)
