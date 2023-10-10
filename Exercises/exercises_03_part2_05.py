import pandas as pd
from os import path

# 3.5.1
# a) Load the four datasets in in ./data/problems/combinel/.
# They contain name (player and team), shot (shots and goals), pass (assists and crosses), and out of bound (throw ins and corners) data.
DATA_DIR = '/Users/maltamirano/Documents/Education/Python-football/code-soccer-files-main/data/problems/combine1'
DATA_DIR2 = '/Users/maltamirano/Documents/Education/Python-football/code-soccer-files-main/data/problems/combine2'
DATA_DIR3 = '/Users/maltamirano/Documents/Education/Python-football/code-soccer-files-main/data'

df_name = pd.read_csv(path.join(DATA_DIR,'name.csv'))
df_shot = pd.read_csv(path.join(DATA_DIR,'shot.csv'))
df_pass = pd.read_csv(path.join(DATA_DIR,'pass.csv'))
df_ob = pd.read_csv(path.join(DATA_DIR,'ob.csv'))

# Combine them: b) using pd. merge. c) using pd. concat.
df_comb1 = pd.merge(df_name, df_shot, how = 'left')
df_comb1 = pd.merge(df_comb1, df_pass, how = 'left')
df_comb1 = pd.merge(df_comb1, df_ob, how = 'left')
df_comb1 = df_comb1.fillna(0)
#print (df_comb1)

# c) using pd. concat.
df_comb2 = pd.concat([df_name.set_index(['player_id', 'match_id']), 
                      df_shot.set_index(['player_id', 'match_id']), 
                      df_pass.set_index(['player_id', 'match_id']), 
                      df_ob.set_index(['player_id', 'match_id'])], 
                      join = 'outer', axis = 1)
df_comb2 = df_comb2.fillna(0)
#print (df_comb2)

# 3.5.2
# a) Load the three datasets in in . /data/problems/combine2/. 
#    It contains the same data, but split "vertically" by position.
df_def = pd.read_csv(path.join(DATA_DIR2,'def.csv'))
df_mid = pd.read_csv(path.join(DATA_DIR2,'mid.csv'))
df_fwd = pd.read_csv(path.join(DATA_DIR2,'fwd.csv'))

# b) Combine them. Make the index of the resulting DataFrame is the default (0, 1, 2, ...)
df_pos = pd.concat([df_def, df_mid, df_fwd], ignore_index = True)
#print (df_pos)

# 3.5.3
# a) Load the team data in . /data/teams.csv.
df_teams = pd.read_csv(path.join(DATA_DIR3,'teams.csv'))

# b) Write a for loop to save subsets of the data frame for each group (A, B, C ...) to the DATA_DIR.
# for group in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
#     (
#         df_teams.query(f"grouping == '{group}'")
#         .to_csv(path.join(DATA_DIR3, f'df_group_{group}.csv'), index = False)
#     )

# c) Then using pd. concat and list comprehensions, 
# lwrite one line of Python that loads these saved subsets and combines them.
df_all_groups = pd.concat([pd.read_csv(path.join(DATA_DIR3, f'df_group_{group}.csv'))
                           for group in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                          ], ignore_index = True)

print (df_all_groups)