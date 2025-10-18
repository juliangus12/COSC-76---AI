from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

def null_heuristic(state):
    return 0

# test 1: two robots swap positions in corridor
print("\ntest 1: two robots swap in corridor")
corridor_maze = Maze("corridor.maz")
mp1 = MazeworldProblem(corridor_maze, (5, 1, 1, 1))
result = astar_search(mp1, mp1.manhattan_heuristic)
print(result)

# test 2: three robots need to reverse their order
print("\ntest 2: three robots reverse order")
with open("corridor3.maz", "w") as f:
    f.write("########\n#......#\n#......#\n########\n\\robot 1 1\n\\robot 3 1\n\\robot 5 1\n")
corridor3_maze = Maze("corridor3.maz")
mp2 = MazeworldProblem(corridor3_maze, (5, 1, 3, 1, 1, 1))
result = astar_search(mp2, mp2.manhattan_heuristic)
print(result)

# test 3: comparing manhattan vs null heuristic
print("\ntest 3: heuristic comparison")
with open("small.maz", "w") as f:
    f.write("......\n......\n.##...\n.##...\n......\n......\n\\robot 0 0\n")
small_maze = Maze("small.maz")
mp3 = MazeworldProblem(small_maze, (5, 5))
result_null = astar_search(mp3, null_heuristic)
result_manhattan = astar_search(mp3, mp3.manhattan_heuristic)
print("null heuristic:", result_null.nodes_visited, "nodes")
print("manhattan heuristic:", result_manhattan.nodes_visited, "nodes")
print(result_manhattan)

# test 4: robots disperse from center to corners
print("\ntest 4: robots spread to corners")
with open("open11x11.maz", "w") as f:
    for i in range(11):
        f.write("." * 11 + "\n")
    f.write("\\robot 5 5\n\\robot 6 5\n\\robot 5 6\n")
open_maze = Maze("open11x11.maz")
mp4 = MazeworldProblem(open_maze, (0, 0, 10, 10, 10, 0))
result = astar_search(mp4, mp4.manhattan_heuristic)
print(result)

# test 5: navigation around obstacles
print("\ntest 5: obstacles and coordination")
maze3 = Maze("maze3.maz")
mp5 = MazeworldProblem(maze3, (3, 3, 2, 4, 1, 4))
result = astar_search(mp5, mp5.manhattan_heuristic)
print(result)
