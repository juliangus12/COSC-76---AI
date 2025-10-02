# foxes.py
# julian gutierrez 25f

from FoxProblem import FoxProblem
from uninformed_search import bfs_search, dfs_search, ids_search

def print_solution(path, algorithm_name, problem=None):
    if path is None:
        print(f"{algorithm_name}: no solution")
        return

    print(f"\n{algorithm_name} found solution in {len(path) - 1} steps:")

    # get totals
    if problem:
        total_chickens = problem.total_chickens
        total_foxes = problem.total_foxes
    else:
        total_chickens = path[0][0]
        total_foxes = path[0][1]

    for i, state in enumerate(path):
        chickens_start, foxes_start, boat_start = state
        chickens_end = total_chickens - chickens_start
        foxes_end = total_foxes - foxes_start
        boat_side = "start" if boat_start == 1 else "end"

        print(f"{i}: {state} - start: {chickens_start}c {foxes_start}f, end: {chickens_end}c {foxes_end}f, boat: {boat_side}")

def test_basic():
    print("testing basic problem (3,3,1)")
    problem = FoxProblem((3, 3, 1))

    bfs_path = bfs_search(problem)
    print_solution(bfs_path, "bfs", problem)

    dfs_path = dfs_search(problem)
    print_solution(dfs_path, "dfs", problem)

    ids_path = ids_search(problem)
    print_solution(ids_path, "ids", problem)

def test_harder():
    print("\ntesting harder problem (5,4,1)")
    problem = FoxProblem((5, 4, 1))

    bfs_path = bfs_search(problem)
    print_solution(bfs_path, "bfs", problem)

    dfs_path = dfs_search(problem, 20)
    print_solution(dfs_path, "dfs", problem)

    ids_path = ids_search(problem)
    print_solution(ids_path, "ids", problem)

def test_model():
    print("testing model")
    problem = FoxProblem((3, 3, 1))

    print(f"start: {problem.get_start_state()}")
    print(f"goal test on start: {problem.is_goal(problem.get_start_state())}")
    print(f"goal test on (0,0,0): {problem.is_goal((0, 0, 0))}")

    # test some states
    legal_states = [(3, 3, 1), (3, 0, 0), (0, 3, 1), (1, 1, 0)]
    illegal_states = [(2, 3, 1), (1, 3, 0)]

    print("legal states:")
    for state in legal_states:
        print(f"  {state}: {problem.is_legal_state(state)}")

    print("illegal states:")
    for state in illegal_states:
        print(f"  {state}: {problem.is_legal_state(state)}")

    print(f"successors of start state:")
    successors = problem.get_successors(problem.get_start_state())
    for successor in successors:
        print(f"  {successor}")

if __name__ == "__main__":
    test_model()
    test_basic()
    test_harder()