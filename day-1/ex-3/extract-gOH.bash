#!/bin/bash
i
for x in $(ls -p | grep "/" )
do
    #Moves to a sub directory.
    cd $x
    #Extracts number of beads from the directory.
    nP=$(echo $x| cut -d . -f 2| cut -d / -f 1)
    #Calculates gOH.
    python /home/eszter/I-PY/i-pi/tools/py/get_rdf.py simulation "xyz" O H 200 0. 2. 0.1
    #nnP=${nP#0}
    #for ((ii=0; ii<$((nnP)); ii++))
    #	do
    #    	if [ $nnP -eq 64 ] && [ $ii -ge 10 ] 
    #            	then
    #    		../xyz2pdb.py simulation.pos_$((ii)).xyz simulation.pos_$((ii)).pdb 
    #    	elif [ $nnP -eq 64 ]
    #            	then
    #    		../xyz2pdb.py simulation.pos_0$((ii)).xyz simulation.pos_0$((ii)).pdb 
    #    	fi
    #done 
#     | trajworks -ipdb -vbox -gr -gr1 O -gr2 H -grmax 2 -hwin gauss-2 -hwinfac 5  > gOH_pdb.data
    cd ..
done

