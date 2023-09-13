#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:47:16 2023

@author: maltamirano
"""

roster = ['ruben dias', 'gabriel jesus', 'riyad mahrez']
print 
roster_dict = {player : len(player)  for player in roster}
roster_dict

i = 0
for player in roster:
    print (roster[i].split()[-1])
    i = i + 1
    
    
    
roster_dict = {'CB': 'ruben dias', 'RW': 'gabriel jesus', 'LW': 'riyah mahrez'}
only_positions = [position for position, name in roster_dict.items()]
only_positions


lastname_starts_j_or_m = [name for position, name in roster_dict.items() if name.split()[-1].startswith('j') or name.split()[-1].startswith('m')]
lastname_starts_j_or_m



def mapper (working_list, working_fn):
   return [working_fn(list_value) for list_value in working_list]
    
match_minutes = [95, 92, 90, 91, 97, 95]

mapper(match_minutes, lambda x: x- 90)



