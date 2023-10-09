import pandas as pd
from os import path

# 3.4.2

# a) Load the player match data into a DataFrame named dfpm.
DATA_DIR  = '/Users/maltamirano/Documents/Education/Python-football/code-soccer-files-main/data'
dfpm = pd.read_csv(path.join(DATA_DIR, 'player_match.csv'))

# b) Figure out the average number of shots and goals each player scored per match.
"""print (dfpm.groupby(['name', 'match_id']).agg(
    shot = ('shot','mean'),
    goal = ('goal','mean')).reset_index() )"""
#print (dfpm.groupby('player_id')['shot','goal'].mean())

# c) Figure out the portion of at players that averaged 4 or more shots per game.
player_ave = dfpm.groupby('player_id').agg(shot = ('shot','mean'))
#print((player_ave['shot'] >= 4).mean())

#3.4.3
# a) Make a new DataFrame dftm that's at the team/match level and includes the following info: 
# match_id, team, total goals, passes, shots and number of players played. 
# The last three columns should be named total_goal, total_pass, total_shot and nplayed respectively.
dftm = dfpm.groupby(['match_id', 'team']).agg(
    total_goals = ('goal', 'sum'),
    total_passes = ('pass', 'sum'),
    total_shots = ('shot', 'sum'),
    nplayed = ('player_id', 'count'))
#print (dftm.head())

#b) Because you grouped by more than one column, note dftm has a multi-index. Make those regular columns.
dftm.reset_index(inplace = True)
#print (dftm.head())

#c) Add a new column boolean no_goals indicating whether or not the team scored 0 goals. Compare average total number of passes and shots for values of no_goals.
dftm['no_goals'] = (dftm['total_goals'] == 0)
#print(dftm.groupby('no_goals')['total_passes','total_shots'].mean())

#d) Run dftm.groupby('match_id' ).count (), compare it with dftm. groupby('match_id').sum()

print(dfpm.groupby('team')['match_id'].sum())
print(dfpm.groupby('team')['match_id'].count())