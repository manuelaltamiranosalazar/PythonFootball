# Modify or create new collumnds of data
import pandas as pd
from os import path
import numpy as np


# 3.1.1 
# Load the player match data into a DataFrame named pm. You'll use it for the rest of the problems in this section.
DATA_DIR = '/Users/maltamirano/Documents/Education/Python-football/code-soccer-files-main/data'
pm = pd.read_csv(path.join(DATA_DIR,'player_match.csv'))
#print(pm.sample(10))

# 3.1.2 
# Add a column to pm, 'ob_ touches' that is number of throw-ins plus number of corners.
pm['ob_touches'] = pm['throw'] + pm['corner']
#print(pm.sample(10))

# 3.1.3 
# Add a column 'player_desc' to pm that takes the form, ' is the ' e.g. 'L. Messi is the Argentina FWD' for Lional Messi.
pm['player_desc'] = pm['name']  + ' is the '  + pm['team'] + ' ' + pm['pos']
#print (pm['player_desc'].sample(10))

# 3.1.4 
# Add a boolean column to pm 'at_least_one_throwin' indicating whether a player had at least one throw-in.
pm['at_least_one_throwin'] = pm['throw'] > 0
#print (pm[['name', 'team', 'throw', 'at_least_one_throwin']].sample(10))

# 3.1.5 
# Add a column 'Len_ last_name' that gives the length of the player's last name.
pm['len_last_name'] = (pm['name'].apply (lambda player_name: len(player_name.split('.')[-1])))
#print (pm[['name', 'len_last_name']].sample(10))

#3.1.6 
# 'match_id' is a numeric (int) column, but it's not really meant for doing math, change it into a string column.
pm['match_id'] = pm['match_id'].astype('str')
#print(pm.dtypes)

# 3.1.7
# a) Let's make the columns in pm more readable. Replace all the ' ' with ' ' in all the columns.
#pm.columns = [column_name.replace('_',' ')  for column_name in pm.columns ]
#print (pm.columns)

# b) This actually isn't good practice. Change it back.
pm.columns = [column_name.replace(' ','_')  for column_name in pm.columns ]
#print (pm.columns)

# 3.1.8
# a) Make a new column 'air_duel_won_percentage' indicating the percentage of a players air duels that a player won.
pm['air_duel_won_percentage'] = pm['air_duel_won'] / pm['air_duel']
#print (pm[['name', 'team', 'air_duel_won', 'air_duel', 'air_duel_won_percentage']].sample(10))

# b) There are missing values in this column, why? Replace all the missing values with -99.
pm['air_duel_won_percentage'].fillna(-1, inplace = True)
#print (pm[['name', 'team', 'air_duel_won', 'air_duel', 'air_duel_won_percentage']].sample(10))

# 3.1.9 
# Drop the column 'air_duel_won_percentage'. In another line, confirm that it worked.
pm.drop('air_duel_won_percentage', axis = 1, inplace = True)
print (pm.columns)