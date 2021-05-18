### CHECKING IF FILES AND DIRECTORIES ARE IN PLACE

import os
dirs     = ['ex-1','ex-2','ex-3','ex-4']
ex1files = ['data.water','in.water','input.xml','water-gas.pdb']
ex1dirs  = []
ex1dirfs = []
ex2files = ['cp2k.in','h2o.xyz','input.xml']
ex2dirs  = ['basis']
ex2dirfs = []
ex3files = ['extract-gOH.bash','extract-pot.bash','extract-kin.bash']
ex3dirs  = ['n.01','n.02','n.04','n.08','n.16','n.32','n.64']
ex3dirfs = ['boxfile','data.lmp','in.lmp','init.chk','input.xml']
ex4files = []
ex4dirs  = ['n.001','n.128']
ex4dirfs = ['boxfile','in.cp2k','init.chk','input.xml','start.chk']

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
           if not all([os.path.isdir(dr+'/'+dd) for dd in globals()[dr[:2]+dr[-1]+'dirs']]):
               misses.extend([dr+'/'+dd+'/' for dd in globals()[dr[:2]+dr[-1]+'dirs']
                              if os.path.isdir(dr+'/'+dd)==False])
               globals()[dr]=False
           if not all([os.path.isfile(dr+'/'+dd+'/'+df) for dd in globals()[dr[:2]+dr[-1]+'dirs']
                       for df in globals()[dr[:2]+dr[-1]+'dirfs']]):    
               misses.extend([dr+'/'+dd+'/'+df for dd in globals()[dr[:2]+dr[-1]+'dirs'] 
                              for df in globals()[dr[:2]+dr[-1]+'dirfs'] 
                              if os.path.isfile(dr+'/'+dd+'/'+df)==False])
               globals()[dr]=False
   
   if misses:
       print(*['You are missing the following files or directories:',
               '---------------------------------------------------',
               *misses],sep='\n')
   
   if all([globals()[dr] for dr in dirs]):
       print('Everything is ready, you can start the tutorial.')
