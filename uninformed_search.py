# cosc 76 pa1 julian 2025
from collections import deque
from SearchSolution import SearchSolution

class SearchNode:

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1


def backchain(node):
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    return list(reversed(path))

def bfs_search(search_problem):
    solution = SearchSolution(search_problem, "BFS")
    
    start_node = SearchNode(search_problem.start_state)
    queue = deque([start_node])
    visited = set()
    visited.add(search_problem.start_state)
    
    while queue:
        node = queue.popleft()
        solution.nodes_visited += 1
        
        if search_problem.goal_test(node.state):
            solution.path = backchain(node)
            return solution
        
        for successor in search_problem.get_successors(node.state):
            if successor not in visited:
                visited.add(successor)
                child = SearchNode(successor, node)
                queue.append(child)
    
    return solution

def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

    solution.nodes_visited += 1
    
    # base case found goal
    if search_problem.goal_test(node.state):
        solution.path = backchain(node)
        return solution
    
    # base case depth limit reached
    if node.depth >= depth_limit:
        return solution
    
    # recursive case check path for loops
    path_states = []
    current = node
    while current is not None:
        path_states.append(current.state)
        current = current.parent
    
    for successor in search_problem.get_successors(node.state):
        if successor not in path_states:
            child = SearchNode(successor, node)
            result = dfs_search(search_problem, depth_limit, child, solution)
            if len(result.path) > 0:
                return result
    
    return solution


def ids_search(search_problem, depth_limit=100):
    for depth in range(depth_limit + 1):
        solution = dfs_search(search_problem, depth)
        if len(solution.path) > 0:
            solution.search_method = "IDS"
            return solution
    
    solution = SearchSolution(search_problem, "IDS")
    return solution