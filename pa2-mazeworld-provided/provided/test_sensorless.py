from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

# test 1: small 4x3 maze
print("\ntest 1: small maze")
maze1 = Maze("maze1.maz")
sp1 = SensorlessProblem(maze1)
result = astar_search(sp1, sp1.manhattan_heuristic)
print(result)

# test 2: larger maze with more complexity
print("\ntest 2: maze3")
maze3 = Maze("maze3.maz")
sp2 = SensorlessProblem(maze3)
result = astar_search(sp2, sp2.manhattan_heuristic)
print(result)

# test 3: custom 6x6 with internal walls
print("\ntest 3: 6x6 with walls")
with open("maze6x6.maz", "w") as f:
    f.write("......\n...#..\n...#..\n...#..\n......\n......\n")
maze6x6 = Maze("maze6x6.maz")
sp3 = SensorlessProblem(maze6x6)
result = astar_search(sp3, sp3.manhattan_heuristic)
print(result)

# test 4: bigger maze for scalability
print("\ntest 4: 8x8 maze")
with open("maze8x8.maz", "w") as f:
    f.write("........\n.##..##.\n.##..##.\n........\n........\n.##..##.\n.##..##.\n........\n")
maze8x8 = Maze("maze8x8.maz")
sp4 = SensorlessProblem(maze8x8)
result = astar_search(sp4, sp4.manhattan_heuristic)
print(result)

# test 5: animated belief state reduction
print("\ntest 5: animation")
maze_anim = Maze("maze1.maz")
sp_anim = SensorlessProblem(maze_anim)
result_anim = astar_search(sp_anim, sp_anim.manhattan_heuristic)
if result_anim.path:
    sp_anim.animate_path(result_anim.path)
    print("localized to:", list(result_anim.path[-1])[0])
