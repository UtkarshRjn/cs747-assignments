from matplotlib import pyplot as plt
import numpy as np

import sys

if(sys.argv[1] == "RP"):
    VP_rand = np.loadtxt("data/cricket/rand_pol.txt")
    POLICY = np.zeros(VP_rand.shape[0]+2,dtype=int)
    POLICY[:-2] = np.array(VP_rand[:,1],dtype = int)

    POLICY[POLICY == 4] = 3
    POLICY[POLICY == 6] = 4


    np.savetxt("RANDPOL.txt",POLICY,fmt='%1d')
elif(sys.argv[1] == "SQ"):
    ourfile = open("vpfile")
    randfile = open("vpfile_rand")


    OS = []
    RS = []

    for l in ourfile:
        OS = list(map(float,l.strip().split()))
        break


    for l in randfile:
        RS = list(map(float,l.strip().split()))
        break

    ourfile.close()
    randfile.close()

    print(sys.argv[2],OS[0],RS[0])

elif(sys.argv[1] == "QP"):
    D = np.loadtxt("QSCORES.txt")    
    plt.plot(D[:,0],D[:,1],label='Optimal Policy')
    plt.plot(D[:,0],D[:,2],label='Random policy')
    plt.xlabel("Value of 'q' ")
    plt.ylabel("Probability of winning")
    plt.legend()
    plt.title("Probability vs B's Strength[Q]")
    plt.savefig("Prob_vs_q.png")
    plt.show()

elif(sys.argv[1] == "runs_plot"):
    OUR = np.loadtxt("vpfile")
    RAND = np.loadtxt("vpfile_rand")

    balls = np.arange(20,0,-1)
    OUR_RUNS = OUR[160:180,0]
    RAND_RUNS = RAND[160:180,0]

    plt.plot(balls,OUR_RUNS,label='Optimal Policy')
    plt.plot(balls,RAND_RUNS,label='Random policy')
    plt.xlabel("Number of Runs")
    plt.ylabel("Probability of winning")
    plt.legend()
    plt.title("Probability of winning in 10 Balls vs Runs left")
    plt.savefig("Prob_vs_runs.png")
    plt.show()    

elif(sys.argv[1] == "balls_plot"):
    OUR = np.loadtxt("vpfile")
    RAND = np.loadtxt("vpfile_rand")

    runs = np.arange(15,0,-1)
    print(runs)
    OUR_RUNS = OUR[20::30,0]
    RAND_RUNS = RAND[20::30,0]

    plt.plot(runs,OUR_RUNS,label='Optimal Policy')
    plt.plot(runs,RAND_RUNS,label='Random policy')
    plt.xlabel("Number of Balls left")
    plt.ylabel("Probability of winning")
    plt.legend()
    plt.title("Probability of hitting 10 runs vs balls left")
    plt.savefig("Prob_vs_balls.png")
    plt.show()    