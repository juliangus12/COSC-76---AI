from MazeworldProblem import MazeworldProblem
from Maze import Maze

from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

# Your additional tests here:

maze1 = Maze("maze1.maz")
maze1.robotloc = [1, 1]
mp1 = MazeworldProblem(maze1, (3, 1))
result1 = astar_search(mp1, mp1.manhattan_heuristic)
print("single robot test:")
print(result1)

maze_corridor = Maze("corridor.maz")
mp2 = MazeworldProblem(maze_corridor, (5, 1, 1, 1))
result2 = astar_search(mp2, mp2.manhattan_heuristic)
print("\ntwo robots swapping positions:")
print(result2)
