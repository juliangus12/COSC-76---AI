# julian
# fall 2025
# cosc 76 pa2

from Maze import Maze
from time import sleep

class SensorlessProblem:

    def __init__(self, maze):
        self.maze = maze
        self.start_state = frozenset(
            (x, y) for x in range(maze.width)
            for y in range(maze.height)
            if maze.is_floor(x, y)
        )

    def __str__(self):
        string = "Blind robot problem: "
        return string

    def goal_test(self, state):
        return len(state) == 1

    def get_successors(self, state):
        successors = []
        actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in actions:
            new_belief = set()
            for x, y in state:
                new_x = x + dx
                new_y = y + dy

                if self.maze.is_floor(new_x, new_y):
                    new_belief.add((new_x, new_y))
                else:
                    new_belief.add((x, y))

            successors.append(frozenset(new_belief))

        return successors

    def manhattan_heuristic(self, state):
        return len(state) - 1

    def animate_path(self, path):
        print("Animating sensorless robot path:\n")

        for step, state in enumerate(path):
            print(f"Step {step}: Belief state has {len(state)} possible locations")

            display = []
            for y in range(self.maze.height - 1, -1, -1):
                row = []
                for x in range(self.maze.width):
                    if not self.maze.is_floor(x, y):
                        row.append('#')
                    elif (x, y) in state:
                        row.append('?')
                    else:
                        row.append('.')
                display.append(''.join(row))

            print('\n'.join(display))
            print()
            sleep(0.5)


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
