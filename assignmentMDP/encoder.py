import argparse
from pulp import *
from typing import *
import numpy as np

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--states", type=str, required=True, help="Path to the cricket states file"
    )
    parser.add_argument(
        "--parameters",
        type=str,
        required=True,
        help="Path to the cricket parameters file",
    )
    parser.add_argument(
        "--q",
        type=float,
        required=True,
        help="The variable controlling the transition probability for player B",
    )

    args = parser.parse_args()
    states: Dict[Tuple[int, int, int], int] = {}
    with open(args.states) as f:
        i = 0
        for line in f:
            line = line.strip()
            # print(line)
            balls = int(line[:2])
            runs = int(line[2:])
            # print(balls, runs)
            if line:
                states[(balls, runs, 0)] = i
                states[(balls, runs, 1)] = i + 1
                i += 2
        states[(0, 0, 0)] = i  # win state
        states[(-1, -1, -1)] = i + 1  # lose state

        numStates = i + 2

    transitions: List[Dict[int, Dict[int, float]]] = [{}, {}]
    q = float(args.q)
    with open(args.parameters) as f:
        i = 0
        for line in f:
            if i == 0:
                i += 1
                continue

            line = line.strip().split()
            line = [float(x) for x in line]
            transitions[0][i - 1] = {-1: line[1],0: line[2],1: line[3],2: line[4],3: line[5],4: line[6],6: line[7],}
            transitions[1][i - 1] = {-1: q,0: (1 - q)/2,1: (1 - q)/2, 2: 0, 3: 0, 4: 0, 6: 0}
            i += 1

        numActions = i - 1

    T = np.zeros((numStates, numActions, numStates))
    R = np.zeros((numStates, numActions, numStates),dtype=int)

    for state, stateNo in states.items():
        balls, runs, player = state

        if stateNo == states[(0, 0, 0)] or stateNo == states[(-1, -1, -1)]:
            continue

        for action, probDict in transitions[player].items():
            for nextRun, prob in probDict.items():
                if nextRun == -1 or (balls == 1 and runs - nextRun > 0):
                    T[stateNo, action, states[(-1, -1, -1)]] += prob
                elif runs - nextRun <= 0:
                    T[stateNo, action, states[(0, 0, 0)]] += prob
                    R[stateNo, action, states[(0, 0, 0)]] = 1
                else:
                    strikeChange = False
                    if(nextRun % 2 == 1 or (balls % 6 == 1)):
                        strikeChange = True

                    if(nextRun % 2 == 1 and (balls % 6 == 1)):
                        strikeChange = False

                    if strikeChange:
                        T[stateNo, action, states[(balls - 1, runs - nextRun, 1- player)]] += prob
                    else:
                        T[stateNo,action,states[(balls - 1, runs - nextRun, player)]] += prob

    print("numStates", numStates)
    print("numActions", numActions)
    print("end", -1)

    for state in range(numStates):
        for action in range(numActions):
            for nextstate in range(numStates):
                if T[state, action, nextstate] != 0:
                    print("transition",state,action,nextstate,R[state, action, nextstate],T[state, action, nextstate])

    print("mdptype", "episodic")
    print("discount", 1.0)