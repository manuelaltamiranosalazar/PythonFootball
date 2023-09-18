import pandas as pd
from os import path 

# 3.2.1 
# Load the player game data into a DataFrame named pm. You'll use it for the rest of the problems in this section.
 
DATA_DIR = '/Users/maltamirano/Documents/Education/Python-football/code-soccer-files-main/data'
pm = pd.read_csv(path.join(DATA_DIR, 'player_match.csv'))
#print (pm.columns)

# 3.2.2 
# Add a column to pm that gives the total number of clearances, crosses, assists and key passes. 
# For each player-game. Do it two ways, one with basic arithmetic operators and another way using a built-in pandas function. 
# Call them 'named _pass1' and 'named _pass2' Prove that they're the same.

pm['named_pass1']  = pm['clearance'] + pm['cross'] + pm['assist'] + pm['keypass']
#print (pm[['name', 'team', 'clearance', 'cross', 'assist', 'keypass', 'named_pass1']].sample(10))

pm['named_pass2'] = (pm[['clearance', 'cross', 'assist', 'keypass']]).sum(axis = 1) 
#print (pm[['name', 'team', 'clearance', 'cross', 'assist', 'keypass', 'named_pass2']].sample(10))

are_the_same = (pm['named_pass1'] == pm['named_pass2']).all()
#print (are_the_same)

# 3.2.3
# a) What were the average values for shots, assists, and passes?
#print ((pm[['shot', 'assist', 'pass']]).mean())

# b) How many times in our data did someone score at least 1 goal and have at least 1 assist?
#print (((pm['goal'] >= 1) & (pm['assist'] >= 1)).sum()) 

# c) What % of player performances was that?
percentage_of_1_goal_and_1_assist = ( ((pm['goal'] >= 1) & (pm['assist'] >= 1)).sum() ) / pm.shape [0]
#print(percentage_of_1_goal_and_1_assist)

# d) How many own goals were there total in our sample?
#print (pm['own_goal'].sum())

# e) What position is most represented in our data? Least?
print ((pm['pos']).value_counts())

