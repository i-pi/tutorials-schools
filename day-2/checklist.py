### CHECKING IF FILES AND DIRECTORIES ARE IN PLACE

import os

dirs  = ['ex-1', 'ex-2', 'ex-3', 'ex-4']
ex1files = ['base.xml', 'data.water', 'in.water']
ex2files = ['data.water', 'in.water', 'piglet.xml']
ex3files = ['data.water', 'in.water', 'npt.xml']
ex4files = ['data.ice', 'data.ice_long', 'data.ice_short', 'highorder.xml', 'in.ice', 'in.ice_long', 'in.ice_short', 'ultimate.xml']

def fileChecker():

   misses = []
   for dr in dirs:
       
       if(os.path.isdir(dr)==False):
           globals()[dr]=False
           misses.extend([dr+'/'])
       else:
           globals()[dr]=True
           if not all([os.path.isfile(dr+'/'+ff) for ff in globals()[dr[:2]+dr[-1]+'files']]):
               misses.extend([dr+'/'+ff for ff in globals()[dr[:2]+dr[-1]+'files'] 
                              if os.path.isfile(dr+'/'+ff)==False])
               globals()[dr]=False
   
   if misses:
       print(*['You are missing the following files or directories:',
               '---------------------------------------------------',
               *misses],sep='\n')
   
   if all([globals()[dr] for dr in dirs]):
       print('Everything is ready, you can start the tutorial.')
