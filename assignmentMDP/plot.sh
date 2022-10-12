#!/bin/bash

python3 plotter.py RP

if [ "$1" == "q" ]
then
    for val in `cat q_values.txt`
    do
        python3 cricket_states.py --balls 15 --runs 30 > statefile
        python3 encoder.py --states statefile --parameters data/cricket/sample-p1.txt --q $val > mdpfile
        python3 planner.py --mdp mdpfile > vpfile
        python3 decoder.py --value-policy vpfile --states statefile > output.txt

        python3 planner.py --policy RANDPOL.txt --mdp mdpfile > vpfile_rand
        
        python3 plotter.py SQ $val >> QSCORES.txt
    done

        python3 plotter.py QP
fi

if [ "$1" == "qf" ]
then
    python3 plotter.py QP
fi

if [ "$1" == "runs" ]
then

        python3 cricket_states.py --balls 15 --runs 30 > statefile
        python3 encoder.py --states statefile --parameters data/cricket/sample-p1.txt --q 0.25 > mdpfile
        python3 planner.py --mdp mdpfile > vpfile

        python3 planner.py --policy RANDPOL.txt --mdp mdpfile > vpfile_rand
        
        python3 plotter.py runs_plot

fi

if [ "$1" == "balls" ]
then

        python3 cricket_states.py --balls 15 --runs 30 > statefile
        python3 encoder.py --states statefile --parameters data/cricket/sample-p1.txt --q 0.25 > mdpfile
        python3 planner.py --mdp mdpfile > vpfile

        python3 planner.py --policy RANDPOL.txt --mdp mdpfile > vpfile_rand
        
        python3 plotter.py balls_plot

fi
