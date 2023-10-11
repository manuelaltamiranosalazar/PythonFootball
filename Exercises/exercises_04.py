import pandas as pd 
from os import path
import sqlite3

DATA_DIR = '/Users/maltamirano/Documents/Education/Python-football/code-soccer-files-main/data'

conn = sqlite3.connect(path.join(DATA_DIR, 'soccer-data.sqlite'))

player_match = pd.read_csv(path.join(DATA_DIR, 'player_match.csv'))
team = pd.read_csv(path.join(DATA_DIR, 'teams.csv'))
player = pd.read_csv(path.join(DATA_DIR, 'players.csv'))

player_match.to_sql('player_match',conn,index = False, if_exists = 'replace')
team.to_sql('team',conn,index = False, if_exists = 'replace')
player.to_sql('player',conn,index = False, if_exists = 'replace')


# 4.1
# a) Using the same sqlite database we were working with in this chapter, 
# use SQL to make a DataFrame that summarizes at shots, goals, and passes at the player-match level. 
# Make it only include players from grouping C. 
# It should have the following columns: date, name, team, goal, shot, pass
# Rename name to player in your query.
qdf_guery_for_df = """SELECT date, name AS player, team.team, goal, shot, pass, grouping
                      FROM player_match, team
                      WHERE team.grouping = 'C'      
                      AND player_match.team = team.team"""
df_group_c = pd.read_sql(qdf_guery_for_df, conn)
#print (df_group_c)

# 4.2
# b) Now modify your query to add in nationality from from player table. 
# Use abbreviations too (t for the team table, pm for player _match, etc).
qdf_guery_for_df = """SELECT date, name AS player, t.team, goal, shot, pass, grouping, p.team as nationality, height, weight
                      FROM player_match AS pm, team AS t, player as p
                      WHERE pm.team = t.team
                      AND pm.player_id= p.player_id
                      AND t.grouping = 'C'"""

df_group_c_nationality = pd.read_sql(qdf_guery_for_df, conn)
print (df_group_c_nationality)