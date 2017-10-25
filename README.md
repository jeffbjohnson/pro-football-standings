# pro-football-standings

This Python program reads a file of season pro football scores and processes this info into overall, conference, and division win-loss records and points for and against of each team. It reads file "NFL Scores.txt" and writes to file "NFL Season Standings.txt".

For example, take the lines of scores below.

Minnesota Vikings 38, Green Bay Packers 10
Chicago Bears 17, Carolina Panthers 3

The output would print Minnesota with records of 1-0 for overall, division, and conference because Minnesota and Green Bay are in the same division, NFC North. The output for Chicago would print records of 1-0 for overall and conference because Chicago and Carolina are in the same, NFC, but not the same division.
