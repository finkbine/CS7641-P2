import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import mlrose
from mlrose import DiscreteOpt


###############
####TSP problem
###############

coords_list1 = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3),(4,7),(3,7)]
coords_list2 = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3),(4,7),(3,7),(2,8),(4,8),(2,9),(5,9),(5,10),(6,10)]

coords_list = coords_list1
if coords_list == coords_list1:num=10;output1="TSP1.png";output2="TSP2.png"
if coords_list == coords_list2:num=16;output1="TSP3.png";output2="TSP4.png"

fitness_coords = mlrose.TravellingSales(coords = coords_list)
problem_fit = mlrose.TSPOpt(length = num, fitness_fn = fitness_coords, maximize=False)

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

max = np.concatenate((-fitness_ga,-fitness_hc,-fitness_mc,-fitness_sa)).max() + 5
x_max = np.concatenate((length_ga,length_hc,length_sa,length_mc)).max()
plt.figure(figsize=(12,8))
plt.plot(length_ga,-fitness_ga,linewidth=6,label="genetic_alg")
plt.plot(length_hc,-fitness_hc+0.1,linewidth=6,label="random_hill_climb")
plt.plot(length_sa,-fitness_sa,linewidth=6,label="simulated_annealing")
plt.plot(length_mc,-fitness_mc,linewidth=6,label="mimic")
plt.title("TSP Problem Fitness, NODE = 10", fontsize=20)
plt.xlabel("Iteration",fontsize=16)
plt.ylabel("Fitness",fontsize=16)
plt.ylim(ymin=5);plt.ylim(ymax=max)
plt.xlim(xmin=0);plt.xlim(xmax=x_max)
plt.legend()
plt.savefig(output1)

all_span = [span_hc,span_sa,span_ga,span_mc]
print(all_span)
####
####

pop=[10,20,30,50,100,200,300,400,500]
xx=[]
for inter in pop:
    x,y,z = mlrose.genetic_alg(problem_fit,
                                              random_state = 2,
                                              curve = True,pop_size= inter
                                            )
    xx.append(y)
plt.figure(figsize=(12, 8))
plt.plot(pop,xx,linewidth=6)
plt.title("TSP Problem Fitness - mimic, NODE = 10", fontsize=20)
plt.xlabel("POP SIZE",fontsize=16)
plt.ylabel("Fitness", fontsize=16)
plt.savefig(output2)

###########################################################################


coords_list1 = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3),(4,7),(3,7)]
coords_list2 = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3),(4,7),(3,7),(2,8),(4,8),(2,9),(5,9),(5,10),(6,10)]

coords_list = coords_list2
if coords_list == coords_list1:num=10;output1="TSP1.png";output2="TSP2.png"
if coords_list == coords_list2:num=16;output1="TSP3.png";output2="TSP4.png"

fitness_coords = mlrose.TravellingSales(coords = coords_list)
problem_fit = mlrose.TSPOpt(length = num, fitness_fn = fitness_coords, maximize=False)

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

max = np.concatenate((-fitness_ga,-fitness_hc,-fitness_mc,-fitness_sa)).max() + 5
x_max = np.concatenate((length_ga,length_hc,length_sa,length_mc)).max()
plt.figure(figsize=(12,8))
plt.plot(length_ga,-fitness_ga,linewidth=6,label="genetic_alg")
plt.plot(length_hc,-fitness_hc+0.1,linewidth=6,label="random_hill_climb")
plt.plot(length_sa,-fitness_sa,linewidth=6,label="simulated_annealing")
plt.plot(length_mc,-fitness_mc,linewidth=6,label="mimic")
plt.title("TSP Problem Fitness, NODE = 16", fontsize=20)
plt.xlabel("Iteration",fontsize=16)
plt.ylabel("Fitness",fontsize=16)
plt.ylim(ymin=5);plt.ylim(ymax=max)
plt.xlim(xmin=0);plt.xlim(xmax=x_max)
plt.legend()
plt.savefig(output1)

all_span = [span_hc,span_sa,span_ga,span_mc]
print(all_span)
####
####

pop=[5,10,20,30,40,50]
xx=[]
for inter in pop:
    x,y,z = mlrose.mimic(problem_fit,
                                              random_state = 2,
                                              curve = True,pop_size= inter
                                            )
    xx.append(y)
plt.figure(figsize=(12, 8))
plt.plot(pop,xx,linewidth=6)
plt.title("TSP Problem Fitness - SA, NODE = 16", fontsize=20)
plt.xlabel("Max Attempts",fontsize=16)
plt.ylabel("Fitness", fontsize=16)
plt.savefig(output2)



#[0.0020058155059814453, 0.0015037059783935547, 0.8065488338470459, 2.1796841621398926]
#[0.008521795272827148, 0.014010190963745117, 0.8817653656005859, 3.7872684001922607]