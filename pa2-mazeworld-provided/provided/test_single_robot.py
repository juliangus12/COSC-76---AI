from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

def null_heuristic(state):
    return 0

# single robot test
test_maze1 = Maze("maze1.maz")
test_maze1.robotloc = [1, 1]
test_mp1 = MazeworldProblem(test_maze1, (3, 1))

print("\nwith null heuristic:")
result = astar_search(test_mp1, null_heuristic)
print(result)

print("\nwith manhattan heuristic:")
result = astar_search(test_mp1, test_mp1.manhattan_heuristic)
print(result)
