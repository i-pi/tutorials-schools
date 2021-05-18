#!/usr/bin/env python

import numpy as np
import sys
import math

xyzfname = sys.argv[1]
pdbfname = sys.argv[2]

xyzf = open(xyzfname,"r")
lines = xyzf.readlines()

for line in lines:
    if(lines.index(line) == 0):
        natoms = int(line[0]) 
nblocks = int(len(lines)/(natoms+2)) 
atom = []
x = []
y = []
z = []
step = []

for line in lines:
    blockindex = math.floor(lines.index(line)/(natoms+2))
    words = line.split()
    if(lines.index(line) == 1):
        cell1 = words[2]
        cell2 = words[3]
        cell3 = words[4]
        angl1 = words[5]
        angl2 = words[6]
        angl3 = words[7]
    if(lines.index(line)%(natoms+2) == 1):
        title1 = words[8]+str('   ')
        title2 = str('   ')+words[10]+str('   ')+words[11]+str('   ')+words[12]+str('   ')+words[13]
    if(lines.index(line)%(natoms+2) == 1):
        step.append(words[9])
    if(lines.index(line)%(natoms+2) >= 2 and lines.index(line)%(natoms+2) <= natoms+1):
        atom.append(words[0])
        x.append(words[1])
        y.append(words[2])
        z.append(words[3])
xyzf.close()

# writing out the .pdb file
pdbf = open(pdbfname,"w")
for index in range(nblocks):
    for line in range(natoms+3):
        if(line%(natoms+3)==0):
            pdbf.write('TITLE    %s %s %s \n'%(title1,step[index],title2))
        elif(line%(natoms+3)==1):
            pdbf.write('CRYST1   %s  %s  %s  %s  %s  %s P 1 \n'%(cell1,cell2,cell3,angl1,angl2,angl3))
        elif(line%(natoms+3)==natoms+2):
            pdbf.write('END \n')
        else:
            nn = index*natoms + line%(natoms+3)-2
            pdbf.write('ATOM    %d    %s   1   1   %s    %s    %s    0.00   0.00     0  \n'%(line%(natoms+3)-1,atom[nn],x[nn],y[nn],z[nn]))


pdbf.close()



