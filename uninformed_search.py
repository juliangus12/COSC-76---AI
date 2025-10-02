# uninformed_search.py
# julian gutierrez 25f

from collections import deque

class SearchNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def bfs_search(search_problem):
    start_state = search_problem.get_start_state()

    if search_problem.is_goal(start_state):
        return [start_state]

    frontier = deque([SearchNode(start_state)])
    visited = {start_state}

    while frontier:
        current_node = frontier.popleft()

        for successor_state in search_problem.get_successors(current_node.state):
            if successor_state not in visited:
                visited.add(successor_state)
                successor_node = SearchNode(successor_state, current_node)

                if search_problem.is_goal(successor_state):
                    return backchain(successor_node)

                frontier.append(successor_node)

    return None

def dfs_search(search_problem, max_depth=float('inf')):
    start_state = search_problem.get_start_state()
    path = [start_state]

    if search_problem.is_goal(start_state):
        return path

    return dfs_recursive(search_problem, start_state, path, max_depth, 0)

def dfs_recursive(search_problem, current_state, path, max_depth, current_depth):
    # base case - max depth
    if current_depth >= max_depth:
        return None

    # try all successors
    for successor_state in search_problem.get_successors(current_state):
        # dont revisit states in current path
        if successor_state not in path:
            new_path = path + [successor_state]

            # base case - found goal
            if search_problem.is_goal(successor_state):
                return new_path

            # recursive case
            result = dfs_recursive(search_problem, successor_state, new_path,
                                 max_depth, current_depth + 1)
            if result is not None:
                return result

    # base case - no solution from this path
    return None

def ids_search(search_problem):
    max_depth = 0

    while max_depth < 1000:
        result = dfs_search(search_problem, max_depth)
        if result is not None:
            return result
        max_depth += 1

    return None

def backchain(node):
    path = []
    current = node

    while current is not None:
        path.append(current.state)
        current = current.parent

    path.reverse()
    return path