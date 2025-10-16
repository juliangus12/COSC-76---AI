"""
Test interesting multi-robot coordination scenarios
"""
from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

def null_heuristic(state):
    return 0

print("=" * 70)
print("SCENARIO 1: Two robots in corridor must pass each other")
print("=" * 70)
print("Description: Two robots in a narrow corridor want to swap positions.")
print("They must coordinate to move around each other.")
print()

corridor_maze = Maze("corridor.maz")
print("Initial maze:")
print(corridor_maze)
print(f"Robots at: A={corridor_maze.robotloc[0:2]}, B={corridor_maze.robotloc[2:4]}")

# Swap positions
mp1 = MazeworldProblem(corridor_maze, (5, 1, 1, 1))
print(f"Goal: A→(5,1), B→(1,1)")
print()

result = astar_search(mp1, mp1.manhattan_heuristic)
print(result)
if result.path:
    print("\nSolution shows robots coordinating to pass:")
    for i, state in enumerate(result.path):
        turn = state[0]
        a_pos = (state[1], state[2])
        b_pos = (state[3], state[4])
        print(f"  Step {i}: Robot {chr(65+turn)}'s turn - A@{a_pos}, B@{b_pos}")
print()

print("=" * 70)
print("SCENARIO 2: Three robots in wrong order in corridor")
print("=" * 70)
print("Description: Three robots are in a corridor in reverse order of their")
print("desired positions. They must coordinate complex movements.")
print()

# Create a wider corridor for 3 robots
with open("corridor3.maz", "w") as f:
    f.write("########\n")
    f.write("#......#\n")
    f.write("#......#\n")
    f.write("########\n")
    f.write("\\robot 1 1\n")
    f.write("\\robot 3 1\n")
    f.write("\\robot 5 1\n")

corridor3_maze = Maze("corridor3.maz")
print("Initial maze:")
print(corridor3_maze)

# Reverse their order
mp2 = MazeworldProblem(corridor3_maze, (5, 1, 3, 1, 1, 1))
print(f"Goal: Reverse order - A→(5,1), B→(3,1), C→(1,1)")
print()

result = astar_search(mp2, mp2.manhattan_heuristic)
print(result)
print()

print("=" * 70)
print("SCENARIO 3: Robots must navigate around obstacles")
print("=" * 70)
print("Description: Multiple robots navigate a maze with obstacles to reach")
print("their goals while avoiding collisions.")
print()

# Use existing maze3
maze3 = Maze("maze3.maz")
print("Maze with obstacles:")
print(maze3)

# Different challenging goal
mp3 = MazeworldProblem(maze3, (3, 4, 2, 3, 1, 3))
print(f"Goal: A→(3,4), B→(2,3), C→(1,3)")
print()

result = astar_search(mp3, mp3.manhattan_heuristic)
print(result)
print()

print("=" * 70)
print("SCENARIO 4: Clustered start, dispersed goal")
print("=" * 70)
print("Description: Robots start clustered together and must spread out")
print("to distant goal positions.")
print()

# Create open area maze
with open("open.maz", "w") as f:
    f.write("...........\n")
    f.write("...........\n")
    f.write("...........\n")
    f.write("...........\n")
    f.write("...........\n")
    f.write("\\robot 5 2\n")
    f.write("\\robot 5 2\n")  # Starting at same spot
    f.write("\\robot 6 2\n")

open_maze = Maze("open.maz")
print("Open area maze:")
print(open_maze)
print("Note: Robots B and C cannot both be at (5,2), so initial state")
print("may have collision. Let's adjust...")

# Fix starting positions to avoid collision
open_maze.robotloc = [5, 2, 6, 2, 7, 2]
mp4 = MazeworldProblem(open_maze, (1, 1, 9, 4, 5, 4))
print(f"Start: Clustered at (5,2), (6,2), (7,2)")
print(f"Goal: Dispersed to (1,1), (9,4), (5,4)")
print()

result = astar_search(mp4, mp4.manhattan_heuristic)
print(result)
print()

print("=" * 70)
print("SCENARIO 5: Single robot in complex maze (baseline)")
print("=" * 70)
print("Description: One robot navigating a complex path, showing baseline")
print("performance without coordination complexity.")
print()

maze1 = Maze("maze1.maz")
maze1.robotloc = [1, 0]
mp5 = MazeworldProblem(maze1, (3, 2))
print("Simple maze:")
print(maze1)
print(f"Goal: (1,0) → (3,2)")
print()

result_null = astar_search(mp5, null_heuristic)
result_manhattan = astar_search(mp5, mp5.manhattan_heuristic)
print("With null heuristic (UCS):")
print(result_null)
print("\nWith Manhattan heuristic:")
print(result_manhattan)
print(f"Improvement: {result_null.nodes_visited - result_manhattan.nodes_visited} fewer nodes visited")
