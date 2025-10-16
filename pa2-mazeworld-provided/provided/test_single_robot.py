from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

# null heuristic for testing
def null_heuristic(state):
    return 0

# Create a simple 1-robot test
# Simple maze from maze1.maz
test_maze1 = Maze("maze1.maz")
print("Maze 1:")
print(test_maze1)

# Create a problem - single robot from (1, 1) to (3, 1)
# We need to manually set the robot location
test_maze1.robotloc = [1, 1]
test_mp1 = MazeworldProblem(test_maze1, (3, 1))

print("Start state:", test_mp1.start_state)
print("Goal:", test_mp1.goal_locations)
print()

# Test with null heuristic (uniform cost search)
print("Testing with null heuristic:")
result = astar_search(test_mp1, null_heuristic)
print(result)

# Test with Manhattan heuristic
print("\nTesting with Manhattan heuristic:")
result = astar_search(test_mp1, test_mp1.manhattan_heuristic)
print(result)
