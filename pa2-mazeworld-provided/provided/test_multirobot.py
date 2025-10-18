from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

def null_heuristic(state):
    return 0

# test 1: three robots simple goal
print("\ntest 1: three robots")
test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)

# test 2: two robots swap
print("\ntest 2: swap positions")
test_maze1 = Maze("maze1.maz")
test_maze1.robotloc = [1, 1, 2, 1]
test_mp2 = MazeworldProblem(test_maze1, (2, 1, 1, 1))
result = astar_search(test_mp2, test_mp2.manhattan_heuristic)
print(result)

# test 3: reaching far goals
print("\ntest 3: far goals")
test_maze3 = Maze("maze3.maz")
test_mp3 = MazeworldProblem(test_maze3, (3, 5, 3, 4, 3, 3))
result = astar_search(test_mp3, test_mp3.manhattan_heuristic)
print(result)
