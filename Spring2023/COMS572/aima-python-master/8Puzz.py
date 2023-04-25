import os.path
import random
import time
from functools import partial
from tkinter import *
import sys

from search import depth_first_graph_search,astar_search, EightPuzzle

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

root = Tk()

state = [4, 5, 6, 3, 3, 2, 7, 8, 0]
puzzle = EightPuzzle(tuple(state))
print(puzzle.find_blank_square(state))
solution = None

def solve():
    """Solves the puzzle using astar_search"""

    return astar_search(puzzle).solution()

def solve_steps():
    """Solves the puzzle step by step"""

    global puzzle
    global solution
    global state
    solution = solve()
    print(solution)

    for move in solution:
        state = puzzle.result(state, move)

def exchange(index):
    """Interchanges the position of the selected tile with the zero tile under certain conditions"""

    global state
    global solution
    global puzzle
    zero_ix = list(state).index(0)
    actions = puzzle.actions(state)
    current_action = ''
    i_diff = index // 3 - zero_ix // 3
    j_diff = index % 3 - zero_ix % 3
    if i_diff == 1:
        current_action += 'DOWN'
    elif i_diff == -1:
        current_action += 'UP'

    if j_diff == 1:
        current_action += 'RIGHT'
    elif j_diff == -1:
        current_action += 'LEFT'

    if abs(i_diff) + abs(j_diff) != 1:
        current_action = ''
    
    if current_action in actions:
        state[zero_ix], state[index] = state[index], state[zero_ix]
        puzzle = EightPuzzle(tuple(state))


def init():
    """Calls necessary functions"""

    global state
    global solution
    state = [4, 5, 6, 3, 3, 2, 7, 8, 0]