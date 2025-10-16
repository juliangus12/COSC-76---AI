"""
Test cases for the Blind Robot (Sensorless) Problem

The robot doesn't know where it starts but knows the maze layout.
Goal: Execute actions to localize the robot to a single position.
"""
from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

print("=" * 80)
print("TEST 1: Small maze (maze1.maz)")
print("=" * 80)
print("A small 4x3 maze to demonstrate basic belief state reduction.\n")

maze1 = Maze("maze1.maz")
print("Maze structure:")
print(maze1)

sp1 = SensorlessProblem(maze1)
print(f"Initial belief state size: {len(sp1.start_state)} possible locations")
print(f"Possible starting positions: {sorted(sp1.start_state)}\n")

result = astar_search(sp1, sp1.manhattan_heuristic)
print(result)

if result.path:
    print("\nFinal localized position:", list(result.path[-1])[0])
    print("\nShowing belief state evolution:")
    for i, state in enumerate(result.path):
        print(f"  Step {i}: {len(state)} possible locations")

print("\n")

print("=" * 80)
print("TEST 2: Slightly larger maze (maze3.maz)")
print("=" * 80)
print("A 5x6 maze with more complex structure.\n")

maze3 = Maze("maze3.maz")
print("Maze structure:")
print(maze3)

sp2 = SensorlessProblem(maze3)
print(f"Initial belief state size: {len(sp2.start_state)} possible locations\n")

result = astar_search(sp2, sp2.manhattan_heuristic)
print(result)

if result.path:
    print("\nFinal localized position:", list(result.path[-1])[0])
    print("\nBelief state reduction:")
    for i, state in enumerate(result.path):
        print(f"  Step {i}: {len(state)} possible locations")

print("\n")

print("=" * 80)
print("TEST 3: Custom 6x6 maze")
print("=" * 80)
print("A 6x6 maze with internal walls for localization.\n")

# Create a 6x6 maze with interesting structure
with open("maze6x6.maz", "w") as f:
    f.write("......\n")
    f.write("...#..\n")
    f.write("...#..\n")
    f.write("...#..\n")
    f.write("......\n")
    f.write("......\n")

maze6x6 = Maze("maze6x6.maz")
print("Maze structure:")
print(maze6x6)

sp3 = SensorlessProblem(maze6x6)
print(f"Initial belief state size: {len(sp3.start_state)} possible locations\n")

result = astar_search(sp3, sp3.manhattan_heuristic)
print(result)

if result.path:
    print("\nFinal localized position:", list(result.path[-1])[0])

print("\n")

print("=" * 80)
print("TEST 4: 8x8 maze with obstacles")
print("=" * 80)
print("Larger maze testing scalability.\n")

# Create an 8x8 maze
with open("maze8x8.maz", "w") as f:
    f.write("........\n")
    f.write(".##..##.\n")
    f.write(".##..##.\n")
    f.write("........\n")
    f.write("........\n")
    f.write(".##..##.\n")
    f.write(".##..##.\n")
    f.write("........\n")

maze8x8 = Maze("maze8x8.maz")
print("Maze structure:")
print(maze8x8)

sp4 = SensorlessProblem(maze8x8)
print(f"Initial belief state size: {len(sp4.start_state)} possible locations\n")

result = astar_search(sp4, sp4.manhattan_heuristic)
print(result)

print("\n")

print("=" * 80)
print("TEST 5: Animation demonstration")
print("=" * 80)
print("Showing animated belief state reduction for maze1.\n")

maze_anim = Maze("maze1.maz")
sp_anim = SensorlessProblem(maze_anim)

result_anim = astar_search(sp_anim, sp_anim.manhattan_heuristic)

if result_anim.path:
    print("Actions taken:")
    action_names = ["North", "South", "East", "West"]

    # Reconstruct actions from state transitions
    print("\nWatching the belief state shrink:\n")
    sp_anim.animate_path(result_anim.path)

    print("Robot successfully localized!")
    print(f"Final position: {list(result_anim.path[-1])[0]}")
