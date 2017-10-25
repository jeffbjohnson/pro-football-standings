from enum import Enum
import operator
        
class ProFootballTeam:
    'Pro Football team class'
    # Initiate each pro football team with 0 wins, losses, and ties
    def __init__(self, teamName, conference, division):
        # self.__key__ = teamName
        self.teamName = teamName
        self.conference = conference
        self.division = division
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.conferenceWins = 0
        self.conferenceLosses = 0
        self.conferenceTies = 0
        self.divisionWins = 0
        self.divisionLosses = 0
        self.divisionTies = 0
        self.pointsFor = 0
        self.pointsVs = 0

    def addWin(self):
        self.wins += 1

    def addLoss(self):
        self.losses += 1

    def addTie(self):
        self.ties += 1
        
    def addConferenceWin(self):
        self.conferenceWins += 1
    
    def addConferenceLoss(self):
        self.conferenceLosses += 1
        
    def addConferenceTie(self):
        self.conferenceTies += 1
        
    def addDivisionWin(self):
        self.divisionWins += 1
    
    def addDivisionLoss(self):
        self.divisionLosses += 1
        
    def addDivisionTie(self):
        self.divisionTies += 1    

    def addPoints(self, our_points, their_points):
       self.pointsFor += our_points
       self.pointsVs += their_points
        
    def getConference(self):
        return self.conference
    
    def getDivision(self):
        return self.division
        
    def printRecord(self):
        return str(self.wins) + '-' + str(self.losses) + '-' + str(self.ties)

    def printConferenceRecord(self):
        return str(self.conferenceWins) + '-' + str(self.conferenceLosses) + '-' \
               + str(self.conferenceTies)

    def printDivisionRecord(self):
        return str(self.divisionWins) + '-' + str(self.divisionLosses) + '-' \
               + str(self.divisionTies)
    
    def getPointsFor(self):
        return self.pointsFor

    def getPointsVs(self):
        return self.pointsVs

# Specify 2 conferences
class Conference(Enum):
    American = 1
    National = 2

# Specify 4 divisions  
class Division(Enum):
    North = 1
    East = 2
    South = 3 
    West = 4
    
if __name__ == '__main__':
    
    # Create a list of ProFootballTeam objects
    teams_list = []
    
    # Initialize each football team with its name, conference, and division
    teams_list.append( ProFootballTeam("Buffalo Bills", Conference.American, Division.East))    
    teams_list.append( ProFootballTeam("Miami Dolphins", Conference.American, Division.East))
    teams_list.append( ProFootballTeam("New England Patriots", Conference.American, Division.East))
    teams_list.append( ProFootballTeam("New York Jets", Conference.American, Division.East))
 
    teams_list.append( ProFootballTeam("Baltimore Ravens", Conference.American, Division.North))
    teams_list.append( ProFootballTeam("Cincinnati Bengals", Conference.American, Division.North))
    teams_list.append( ProFootballTeam("Cleveland Browns", Conference.American, Division.North))
    teams_list.append( ProFootballTeam("Pittsburgh Steelers", Conference.American, Division.North))

    teams_list.append( ProFootballTeam("Houston Texans", Conference.American, Division.South))
    teams_list.append( ProFootballTeam("Indianapolis Colts", Conference.American, Division.South))
    teams_list.append( ProFootballTeam("Jacksonville Jaguars", Conference.American, Division.South))
    teams_list.append( ProFootballTeam("Tennessee Titans", Conference.American, Division.South))
    
    teams_list.append( ProFootballTeam("Denver Broncos", Conference.American, Division.West))
    teams_list.append( ProFootballTeam("Kansas City Chiefs", Conference.American, Division.West))
    teams_list.append( ProFootballTeam("Oakland Raiders", Conference.American, Division.West))
    teams_list.append( ProFootballTeam("San Diego Chargers", Conference.American, Division.West))
    
    teams_list.append( ProFootballTeam("Dallas Cowboys", Conference.National, Division.East))
    teams_list.append( ProFootballTeam("New York Giants", Conference.National, Division.East))
    teams_list.append( ProFootballTeam("Philadelphia Eagles", Conference.National, Division.East))    
    teams_list.append( ProFootballTeam("Washington Redskins", Conference.National, Division.East))
    
    teams_list.append( ProFootballTeam("Chicago Bears", Conference.National, Division.North))
    teams_list.append( ProFootballTeam("Detroit Lions", Conference.National, Division.North))
    teams_list.append( ProFootballTeam("Green Bay Packers", Conference.National, Division.North))
    teams_list.append( ProFootballTeam("Minnesota Vikings", Conference.National, Division.North))
    
    teams_list.append( ProFootballTeam("Atlanta Falcons", Conference.National, Division.South))
    teams_list.append( ProFootballTeam("Carolina Panthers", Conference.National, Division.South))
    teams_list.append( ProFootballTeam("New Orleans Saints", Conference.National, Division.South))    
    teams_list.append( ProFootballTeam("Tampa Bay Buccaneers", Conference.National, Division.South))
    
    teams_list.append( ProFootballTeam("Arizona Cardinals", Conference.National, Division.West))
    teams_list.append( ProFootballTeam("Los Angeles Rams", Conference.National, Division.West))
    teams_list.append( ProFootballTeam("San Francisco 49ers", Conference.National, Division.West))
    teams_list.append( ProFootballTeam("Seattle Seahawks", Conference.National, Division.West))      
 
    # Open "NFL Scores.txt" file to read season football scores
    with open("NFL Scores.txt", 'r') as in_file:
        for line in in_file:
            try:
                # Replace tab and newline with space
                line = line.replace('[\t\n]', ' ')
                # Delete the strings below from end of score lines
                line = line.replace("at London, England", "")
                line = line.replace("at Mexico City, Mexico", "")
                line = line.replace("(OT)", "")
                
                # Print each modified line score on console to review
                print(line)
                
                # Split score into 2 teams
                winner, loser = line.split(',')
                # Split winner and loser phrases into lists
                winner_list = winner.split()
                loser_list = loser.split()
                
                # Convert points, at end of list, to int
                teamA_points = int(winner_list[-1])
                teamB_points = int(loser_list[-1])
                
                # Join words of each team into a string
                teamA = " ".join(winner_list[:-1])
                teamB = " ".join(loser_list[:-1])
                            
                # if 2nd team has more points, switch teams A and B
                if (teamA_points < teamB_points):
                    teamA, teamB = teamB, teamA
                    teamA_points, teamB_points = teamB_points, teamA_points
            
                # Iterate through teams list to find index of winner, loser
                for index, team in enumerate(teams_list):
                    if team.teamName == teamA:
                        index1 = index
                    if team.teamName == teamB:
                        index2 = index
                        
                # Add points for and against for both teams     
                teams_list[index1].addPoints(teamA_points, teamB_points)
                teams_list[index2].addPoints(teamB_points, teamA_points)
                
                # Determine if game was win or tie
                if (teamA_points > teamB_points):                
                    teams_list[index1].addWin()
                    teams_list[index2].addLoss()
                        
                    # Add a conference win/loss if both teams have same conference
                    if teams_list[index1].getConference() == teams_list[index2].getConference():
                        teams_list[index1].addConferenceWin()
                        teams_list[index2].addConferenceLoss()
                        
                        # Add a division win/loss if both teams also have same division
                        if teams_list[index1].getDivision() == teams_list[index2].getDivision():
                            teams_list[index1].addDivisionWin()
                            teams_list[index2].addDivisionLoss()
                                     
                # Add a tie for each team if they tied
                else:
                    teams_list[index1].addTie()
                    teams_list[index2].addTie()
                    
                     # Add a conference tie if both teams have same conference
                    if teams_list[index1].getConference() == teams_list[index2].getConference():
                        teams_list[index1].addConferenceTie()
                        teams_list[index2].addConferenceTie()
                        # Add a division tie if both teams also have same division
                        if teams_list[index1].getDivision() == teams_list[index2].getDivision():
                            teams_list[index1].addDivisionTie()
                            teams_list[index2].addDivisionTie()
                
            # Print an error if a file line couldn't be processed
            except:
                print("Error in line of file")
                
    # Create list of each division 
    american_east = []
    american_north = []
    american_south = []
    american_west = []
    national_east = []
    national_north = []
    national_south = []
    national_west = []
    
    # Create a list for each NFL division
    for team in teams_list:
        if team.conference == Conference.American:
            if team.division == Division.East:
                american_east.append(team)
            elif team.division == Division.North:
                american_north.append(team)
            elif team.division == Division.South:
                american_south.append(team)
            elif team.division == Division.West:
                american_west.append(team)
                
        if team.conference == Conference.National:
            if team.division == Division.East:
                national_east.append(team)
            elif team.division == Division.North:
                national_north.append(team)
            elif team.division == Division.South:
                national_south.append(team)
            elif team.division == Division.West:
                national_west.append(team)
                
    # Close input file
    in_file.close()
    
    # Return specified # of spaces          
    def spaces(number):
        return ' ' * number
    # Return specified # of dashes
    def dashes(number):
        return '-' * number
    
    # Sort teams by records overall, division, conference, respectively
    def sort_record(division_list):
        return division_list.sort(key=operator.attrgetter('wins', 'divisionWins', 'conferenceWins'), \
                             reverse=True)
    # Create and open output file
    out_file = open("NFL Season Standings.txt", 'w')  
    
    # Call sort_record function for each division
    sort_record(american_east)
    sort_record(american_north)
    sort_record(american_south)
    sort_record(american_west)
    
    sort_record(national_east)
    sort_record(national_north)
    sort_record(national_south)
    sort_record(national_west)    
    
    # Set print format for overall, division, conference records            
    def print_team_records(team):
        record = team.printRecord()
        conferenceRecord = team.printConferenceRecord()
        divisionRecord = team.printDivisionRecord()
        pointsFor = team.getPointsFor()
        pointsVs = team.getPointsVs()
        out_file.write(("{:<20}" + spaces(3)+ "{:>6}" + spaces(3) + "{:>6}" + spaces(5) + "{:>6}" + spaces(6) \
              + "{:^3}" + spaces(6) + "{:^3}\n").format(team.teamName, record, divisionRecord, \
              conferenceRecord, pointsFor, pointsVs))    
    
    # Print this header for each division
    def print_header(divName):
        out_file.write("\n " + divName + spaces(13) + "Overall" + spaces(2)  + "Division" \
              + spaces(2) + "Conference" + spaces(2) + "Pts_For" + spaces(2) \
              + "Pts_Vs\n")
        out_file.write(dashes(68) + '\n')
        
    # Print header and teams by record for each division
    print_header("AFC East")    
    for team in american_east:
        print_team_records(team)
    
    print_header("AFC North")
    for team in american_north:
        print_team_records(team)
        
    print_header("AFC South")
    for team in american_south:
        print_team_records(team)
        
    print_header("AFC West")    
    for team in american_west:
        print_team_records(team)
        
    print_header("NFC East")   
    for team in national_east:
        print_team_records(team)

    print_header("NFC North")
    for team in national_north:
        print_team_records(team)
        
    print_header("NFC South")
    for team in national_south:
        print_team_records(team)
        
    print_header("NFC West")  
    for team in national_west:
        print_team_records(team)