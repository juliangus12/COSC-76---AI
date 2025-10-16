# julian
# fall 2025
# cosc 76 pa2

from Maze import Maze
from time import sleep

class MazeworldProblem:

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        # state format: (robot_turn, x0, y0, x1, y1, ...)
        num_robots = len(maze.robotloc) // 2
        self.start_state = tuple([0] + maze.robotloc)
        self.num_robots = num_robots

    def __str__(self):
        string = "Mazeworld problem: "
        string += str(self.num_robots) + " robots, "
        string += "goal: " + str(self.goal_locations)
        return string

    def goal_test(self, state):
        return state[1:] == self.goal_locations

    def get_successors(self, state):
        successors = []
        robot_turn = state[0]

        robot_idx = robot_turn * 2 + 1
        x = state[robot_idx]
        y = state[robot_idx + 1]

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]

        for dx, dy in moves:
            new_x = x + dx
            new_y = y + dy

            if self.maze.is_floor(new_x, new_y):
                collision = False
                for i in range(self.num_robots):
                    if i != robot_turn:
                        other_idx = i * 2 + 1
                        if state[other_idx] == new_x and state[other_idx + 1] == new_y:
                            collision = True
                            break

                if not collision:
                    new_state = list(state)
                    new_state[robot_idx] = new_x
                    new_state[robot_idx + 1] = new_y
                    new_state[0] = (robot_turn + 1) % self.num_robots
                    successors.append(tuple(new_state))

        return successors

    def manhattan_heuristic(self, state):
        total = 0
        for i in range(self.num_robots):
            robot_idx = i * 2 + 1
            goal_idx = i * 2
            current_x = state[robot_idx]
            current_y = state[robot_idx + 1]
            goal_x = self.goal_locations[goal_idx]
            goal_y = self.goal_locations[goal_idx + 1]
            total += abs(current_x - goal_x) + abs(current_y - goal_y)
        return total

    def animate_path(self, path):
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
