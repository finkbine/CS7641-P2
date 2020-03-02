import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import mlrose
from mlrose import DiscreteOpt

fitness = mlrose.ContinuousPeaks(t_pct=0.1)
size1 = 50
size2 = 100

size  = size1

if size==50: output1="CPP1.png";output2="CPP2.png"
if size==100:output1="CPP3.png";output2="CPP4.png"

problem_fit = mlrose.DiscreteOpt(size, fitness, maximize=True, max_val=2)


start_time = time.time()
a1,b1,c1  = mlrose.genetic_alg(problem_fit,   mutation_prob = 0.2,
                                              max_attempts = 10, random_state = 2,
                                              curve = True,
                                               )
span_ga = time.time() - start_time
fitness_ga = c1
length_ga = list(range(1,c1.shape[0]+1))


start_time = time.time()
a2,b2,c2  = mlrose.random_hill_climb(problem_fit,
                                              random_state = 2,
                                              curve = True,
                                            )
span_hc = time.time() - start_time
fitness_hc = c2
length_hc = list(range(1,c2.shape[0]+1))


start_time = time.time()
a3,b3,c3  = mlrose.simulated_annealing(problem_fit,
                                              random_state = 2,
                                              curve = True,
                                            )
span_sa = time.time() - start_time
fitness_sa = c3
length_sa = list(range(1,c3.shape[0]+1))

start_time = time.time()
a4,b4,c4  = mlrose.mimic(problem_fit,
                                              random_state = 2,
                                              curve = True,
                                            )
span_mc = time.time() - start_time
fitness_mc = c4
length_mc = list(range(1,c4.shape[0]+1))

max = np.concatenate((fitness_ga,fitness_hc,fitness_mc,fitness_sa)).max() + 5
x_max = np.concatenate((length_ga,length_hc,length_sa,length_mc)).max()
plt.figure(figsize=(12,8))
plt.plot(length_ga,fitness_ga,linewidth=6,label="genetic_alg")
plt.plot(length_hc,fitness_hc+2,linewidth=6,label="random_hill_climb")
plt.plot(length_sa,fitness_sa,linewidth=6,label="simulated_annealing")
plt.plot(length_mc,fitness_mc,linewidth=6,label="mimic")
plt.title("Continuous Peaks Problem Fitness, SIZE = 50", fontsize=20)
plt.xlabel("Iteration",fontsize=16)
plt.ylabel("Fitness",fontsize=16)
plt.ylim(ymin=5);plt.ylim(ymax=max)
plt.xlim(xmin=0);plt.xlim(xmax=x_max)
plt.legend()
plt.savefig(output1)

all_span = [span_hc,span_sa,span_ga,span_mc]
print(all_span)
print(fitness_hc)
####
####

pop=[10,20,30,50,100,200,300,400,500]
xx=[]
for inter in pop:
    x,y,z = mlrose.mimic(problem_fit,
                                              random_state = 2,
                                              curve = True,pop_size= inter
                                            )
    xx.append(y)
plt.figure(figsize=(12, 8))
plt.plot(pop,xx,linewidth=6)
plt.title("Continuous Peaks Problem Fitness - mimic, SIZE = 50 ", fontsize=20)
plt.xlabel("POP SIZE",fontsize=16)
plt.ylabel("Fitness", fontsize=16)
plt.savefig(output2)

#######################################################

fitness = mlrose.ContinuousPeaks(t_pct=0.1)
size1 = 50
size2 = 100

size  = size2

if size==50: output1="CPP1.png";output2="CPP2.png"
if size==100:output1="CPP3.png";output2="CPP4.png"

problem_fit = mlrose.DiscreteOpt(size, fitness, maximize=True, max_val=2)


start_time = time.time()
a1,b1,c1  = mlrose.genetic_alg(problem_fit,   mutation_prob = 0.2,
                                              max_attempts = 10, random_state = 2,
                                              curve = True,
                                               )
span_ga = time.time() - start_time
fitness_ga = c1
length_ga = list(range(1,c1.shape[0]+1))


start_time = time.time()
a2,b2,c2  = mlrose.random_hill_climb(problem_fit,
                                              random_state = 2,
                                              curve = True,
                                            )
span_hc = time.time() - start_time
fitness_hc = c2
length_hc = list(range(1,c2.shape[0]+1))


start_time = time.time()
a3,b3,c3  = mlrose.simulated_annealing(problem_fit,
                                              random_state = 2,
                                              curve = True,
                                            )
span_sa = time.time() - start_time
fitness_sa = c3
length_sa = list(range(1,c3.shape[0]+1))

start_time = time.time()
a4,b4,c4  = mlrose.mimic(problem_fit,
                                              random_state = 2,
                                              curve = True,
                                            )
span_mc = time.time() - start_time
fitness_mc = c4
length_mc = list(range(1,c4.shape[0]+1))

max = np.concatenate((fitness_ga,fitness_hc,fitness_mc,fitness_sa)).max() + 5
x_max = np.concatenate((length_ga,length_hc,length_sa,length_mc)).max()
plt.figure(figsize=(12,8))
plt.plot(length_ga,fitness_ga,linewidth=6,label="genetic_alg")
plt.plot(length_hc,fitness_hc+2,linewidth=6,label="random_hill_climb")
plt.plot(length_sa,fitness_sa,linewidth=6,label="simulated_annealing")
plt.plot(length_mc,fitness_mc,linewidth=6,label="mimic")
plt.title("Continuous Peaks Problem Fitness, SIZE = 100", fontsize=20)
plt.xlabel("Iteration",fontsize=16)
plt.ylabel("Fitness",fontsize=16)
plt.ylim(ymin=5);plt.ylim(ymax=max)
plt.xlim(xmin=0);plt.xlim(xmax=x_max)
plt.legend()
plt.savefig(output1)

all_span = [span_hc,span_sa,span_ga,span_mc]
print(all_span)
print(fitness_hc)
####
####

pop=[10,20,30,50,100,200,300,400,500]
xx=[]
for inter in pop:
    x,y,z = mlrose.mimic(problem_fit,
                                              random_state = 2,
                                              curve = True,pop_size= inter
                                            )
    xx.append(y)
plt.figure(figsize=(12, 8))
plt.plot(pop,xx,linewidth=6)
plt.title("Continuous Peaks Problem Fitness - mimic, SIZE = 100", fontsize=20)
plt.xlabel("POP SIZE",fontsize=16)
plt.ylabel("Fitness", fontsize=16)
plt.savefig(output2)


###[0.0, 0.031249046325683594, 0.45435404777526855, 18.183030366897583]
###[0.0010004043579101562, 0.16399812698364258, 1.4152166843414307, 76.18003797531128]
