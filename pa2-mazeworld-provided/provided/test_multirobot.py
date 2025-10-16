from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

def null_heuristic(state):
    return 0

print("=" * 60)
print("TEST 1: Three robots - simple goal")
print("=" * 60)
test_maze3 = Maze("maze3.maz")
print("Initial maze:")
print(test_maze3)
print(f"Robot starting positions: {test_maze3.robotloc}")

# Goal: move robots slightly
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
print(f"Start state: {test_mp.start_state}")
print(f"Goal: {test_mp.goal_locations}")

result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
print()

print("=" * 60)
print("TEST 2: Two robots must coordinate to swap positions")
print("=" * 60)
# Create a narrow corridor scenario
test_maze1 = Maze("maze1.maz")
# Two robots in a corridor that need to swap
test_maze1.robotloc = [1, 1, 2, 1]
test_mp2 = MazeworldProblem(test_maze1, (2, 1, 1, 1))
print("Initial positions: robots at (1,1) and (2,1)")
print("Goal: swap to (2,1) and (1,1)")
print(f"Start: {test_mp2.start_state}")

result = astar_search(test_mp2, test_mp2.manhattan_heuristic)
print(result)
if result.path:
    print("\nPath details:")
    for i, state in enumerate(result.path):
        print(f"Step {i}: {state}")
print()

print("=" * 60)
print("TEST 3: Three robots - reaching far goals")
print("=" * 60)
test_maze3 = Maze("maze3.maz")
# Move all robots to opposite corners/positions
test_mp3 = MazeworldProblem(test_maze3, (3, 5, 3, 4, 3, 3))
print(f"Start: robots at {test_maze3.robotloc}")
print(f"Goal: robots at (3,5), (3,4), (3,3)")

result = astar_search(test_mp3, test_mp3.manhattan_heuristic)
print(result)
print()
