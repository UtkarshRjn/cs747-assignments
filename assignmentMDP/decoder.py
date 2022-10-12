import argparse
from typing import *
import math

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--value-policy", type=str, required=True, help="Path to the value_policy_file"
    )
    parser.add_argument(
        "--states", type=str, required=True, help="Path to the statesfilepath file"
    )

    args = parser.parse_args()

    states: Dict[int, str] = {}
    with open(args.states) as f:
        i = 0
        for line in f:
            line = line.strip()
            states[i] = line
            i += 2

    with open(args.value_policy) as f:
        j = 0
        for line in f:
            if j % 2 == 1:
                j += 1
                continue

            if j >= i:
                break

            line = line.strip().split()
            if(line[1] == '3'): line[1] = '4'
            elif(line[1] == '4'): line[1] = '6'


            print(states[j], line[1], float(line[0]))
            j += 1
