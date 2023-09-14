from os import path 
import pandas as pd

DATA_DIR = '/Users/maltamirano/Documents/Education/Python-football/code-soccer-files-main/data'

#3.0.1
#Load the match data into a DataFrame named match. You'll use it for the rest of the problems in this section.
match = pd.read_csv(path.join(DATA_DIR, 'matches.csv'))
#print(type(match))

#3.0.2
#Use the match DataFrame to create another DataFrame, match10, that is the first 10 matches (e.g. the 10 matches with the earliest dates).
  
match10 = match.sort_values('date').head(10)
#print(match10)

#3.0.3
#Sort match by label in descending order (so Uruguay - Saudi Arabia is on the first line).. On another line, look at match in the REPL and make sure it worked.
#print(match.sort_values('label', ascending = False))
#print(type(match.sort_values('label')))

#3.0.5
#a) Make a new DataFrame, match_simple, with just the columns 'date', 'home_team','away_team', 'home_score' and 'away_score' in that order.
match_simple = match[['date', 'home_team','away_team', 'home_score', 'away_score']]
#print(match_simple)

#b) Rearrange match_simple so the order is 'home_team', 'away_team','date', 'home_ score" , 'away_score'
match_simple = match_simple[['home_team', 'away_team','date', 'home_score' , 'away_score']]
#print(match_simple)

#c) Using the original match DataFrame, add the 'match_id' column to match_simple.
match_simple['match_id'] = match['match_id']
#print(match_simple)

#d) Write a copy of match_simple to your computer, match_simple. txt that is ' | ' (pipe) delimited instead of ','(comma) delimited.
#match_simple.to_csv(path.join(DATA_DIR,'match_simple.txt'),sep = '|', index = False)

match_simple_txt = pd.read_csv(path.join(DATA_DIR,'match_simple.txt'))
print(match_simple_txt.head())
print(type(match_simple_txt))