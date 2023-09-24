import pandas as pd
import numpy as np
from os import path

# 3.3.1 
# Load the player data from into a DataFrame named dfp. You'll use it for the rest of the problems in this section.
DATA_DIR = '/Users/maltamirano/Documents/Education/Python-football/code-soccer-files-main/data'
dfp = pd.read_csv(path.join(DATA_DIR, 'players.csv'))
#print (dfp.head())


# 3.3.2 
# Make smaller DataFrame with just Brazilian players and only the columns: 'player_name',
# 'pos', 'foot', 'weight', 'height'. Do it two ways: (a) using the loc syntax, and (b) 
# another time using the query syntax. Call them dfp_bral and dfp_bra2.
is_brazilian = dfp['team'] == 'Brazil'
dfp_bra1 = dfp.loc[is_brazilian, ['player_name', 'pos', 'foot', 'weight', 'height']]
#print (dfp_bra1)


# and (b) another time using the query syntax. Call them dfp_bral and dfp_bra2.
dfp_bra2 = dfp.query("team == 'Brazil'")[['player_name', 'pos', 'foot', 'weight', 'height']]
#print (dfp_bra2)

# 3.3.3 
# Make a DataFrame dfp_no_bra with the same columns that is everyone EXCEPT Brazilian players, 
# add the 'nationality' column to it.
nationality = np.nan
dfp_no_bra = dfp.loc[dfp['team'] != 'Brazil', ['player_name', 'pos', 'foot', 'weight', 'height']] 
dfp_no_bra['nationality'] = dfp['team']
#print (dfp_no_bra.sample(20)) 

# 3.3.4
# a) Are there any duplicates by birth day dfp DataFrame? Hint: remember people born in different years can have the same birthday.
dfp['bday'] = dfp['birth_date'].astype(str).str[-4:]
#print(dfp['bday'].duplicated().any())

# b) Divide df pinto two separate Dataframesd fp_dups and dfp_nodups, one with dups (birthday)
#one without.
dups = dfp['bday'].duplicated(keep = False)
fp_dups  = dfp.loc[dups]
fp_no_dups  = dfp.loc[~dups]

#print (fp_dups)
#print (fp_no_dups)

# 3.3.5 Add a new column to dfp called 'height _description' with the values:
# • 'tall' for players whose height is greater than 195 cm
# • 'short' for players less than 175 cm
# • missing otherwise
height_description = np.nan
dfp.loc[dfp['height'] < 175, 'height_description'] = 'Short'
dfp.loc[dfp['height'] > 195, 'height_description'] = 'Tall'
#print (dfp.sample(20))

#3.3.6 
# Make a new DataFrame with only observations for which 'height_description' is missing.
# Do this with both the (a) loc and 
dfp_no_height_desc1 = dfp.loc[dfp['height_description'].isnull()]
#print (dfp_no_height_desc1).sample(10)

# (b) query syntax. Call them dfp_no_descland dfp_no_desc2.
dfp_no_height_desc2 = dfp.query("height_description.isnull()")
print (dfp_no_height_desc2.sample(10))