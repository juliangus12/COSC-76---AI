from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

def null_heuristic(state):
    return 0

# test 1: two robots pass in corridor
print("\ntest 1: corridor swap")
corridor_maze = Maze("corridor.maz")
mp1 = MazeworldProblem(corridor_maze, (5, 1, 1, 1))
result = astar_search(mp1, mp1.manhattan_heuristic)
print(result)

# test 2: three robots reverse order
print("\ntest 2: reverse order")
with open("corridor3.maz", "w") as f:
    f.write("########\n#......#\n#......#\n########\n\\robot 1 1\n\\robot 3 1\n\\robot 5 1\n")
corridor3_maze = Maze("corridor3.maz")
mp2 = MazeworldProblem(corridor3_maze, (5, 1, 3, 1, 1, 1))
result = astar_search(mp2, mp2.manhattan_heuristic)
print(result)

# test 3: navigate with obstacles
print("\ntest 3: obstacles")
maze3 = Maze("maze3.maz")
mp3 = MazeworldProblem(maze3, (3, 4, 2, 3, 1, 3))
result = astar_search(mp3, mp3.manhattan_heuristic)
print(result)

# test 4: clustered to dispersed
print("\ntest 4: disperse")
with open("open.maz", "w") as f:
    f.write("...........\n...........\n...........\n...........\n...........\n\\robot 5 2\n\\robot 6 2\n\\robot 7 2\n")
open_maze = Maze("open.maz")
mp4 = MazeworldProblem(open_maze, (1, 1, 9, 4, 5, 4))
result = astar_search(mp4, mp4.manhattan_heuristic)
print(result)

# test 5: single robot baseline
print("\ntest 5: single robot")
maze1 = Maze("maze1.maz")
maze1.robotloc = [1, 0]
mp5 = MazeworldProblem(maze1, (3, 2))
result_null = astar_search(mp5, null_heuristic)
result_manhattan = astar_search(mp5, mp5.manhattan_heuristic)
print("null:", result_null.nodes_visited, "nodes")
print("manhattan:", result_manhattan.nodes_visited, "nodes")
print(result_manhattan)
