import sys
import time
from search import EightPuzzle
from search import astar_search
from search import breadth_first_graph_search
from search import iterative_deepening_search



file_name = sys.argv[1]
algorithm_name = sys.argv[2]

File=open("OutputForFile3Level24.txt","a") 

with open(file_name, 'r') as file:
    numbers = list(file.read().split())

for i in range(len(numbers)):
    if numbers[i]=='_':
        numbers[i]='0'

initial_state = tuple(map(int, numbers))
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
problem = EightPuzzle(initial_state, goal_state)


if(problem.check_solvability(initial_state)==False):
    File.write("\nSolution Doesn't Exist, stopping execution")
    File.write("\n...............Ran the FILE "+file_name+" on ALGORITHM "+algorithm_name+".........................\n\n\n")
    print("Solution Doesn't Exist, stopping execution")
    exit()

if algorithm_name=="h1":
    result = astar_search(problem,display=True)
    if result:
        File.write("\nPath Length: "+str(result.depth))
        File.write("\nPath: "+str(result.solution()))
        print(f'Path Length {result.depth}')
        print("Path: "+str(result.solution()))
    else:
        print("Total nodes generated: undefined")
        print("Time out, more than 15 minutes")
        print("Path Length: Timed Out")
        print("Path sequence: Timed out")

elif algorithm_name=="h2":
    result = astar_search(problem,problem.man,display=True)
    if result:
        File.write("\nPath Length: "+str(result.depth))
        File.write("\nPath: "+str(result.solution()))
        print(f'Path Length {result.depth}')
        print("Path: "+str(result.solution()))
    else:
        File.write("\nTotal nodes generated: undefined\nTime out, more than 15 minutes\nPath Length: Timed Out\nPath sequence: Timed out\n")
        print("Total nodes generated: undefined")
        print("Time out, more than 15 minutes")
        print("Path Length: Timed Out")
        print("Path sequence: Timed out")

elif algorithm_name=="h3":
    result = astar_search(problem,problem.h3,display=True)
    if result:
        File.write("\nPath Length: "+str(result.depth))
        File.write("\nPath: "+str(result.solution()))
        print(f'Path Length {result.depth}')
        print("Path: "+str(result.solution()))
    else:
        File.write("\nTotal nodes generated: undefined\nTime out, more than 15 minutes\nPath Length: Timed Out\nPath sequence: Timed out\n")
        print("Total nodes generated: undefined")
        print("Time out, more than 15 minutes")
        print("Path Length: Timed Out")
        print("Path sequence: Timed out")


elif algorithm_name=="BFS":
    result = breadth_first_graph_search(problem)
    if result:
        File.write("\nPath Length: "+str(result.depth))
        File.write("\nPath: "+str(result.solution()))
        print(f'Path Length {result.depth}')
        print("Path: "+str(result.solution()))
    else:
        File.write("\nTotal nodes generated: undefined\nTime out, more than 15 minutes\nPath Length: Timed Out\nPath sequence: Timed out\n")
        print("Total nodes generated: undefined")
        print("Time out, more than 15 minutes")
        print("Path Length: Timed Out")
        print("Path sequence: Timed out")

elif algorithm_name=="IDS":
    result,num_of_nodes= iterative_deepening_search(problem)
    if result:
        File.write("\nPath Length: "+str(result.depth))
        File.write("\nPath: "+str(result.solution()))
        print(f'Path Length {result.depth}')
        print("Path: "+str(result.solution()))
    else:
        File.write("\nTotal nodes generated: undefined\nTime out, more than 15 minutes\nPath Length: Timed Out\nPath sequence: Timed out")
        print("Total nodes generated: undefined")
        print("Time out, more than 15 minutes")
        print("Path Length: Timed Out")
        print("Path sequence: Timed out")


File.write("\n...............Ran the FILE "+file_name+" on ALGORITHM "+algorithm_name+".........................\n\n\n")

import winsound
duration=3000
freq=500
winsound.Beep(freq,duration)