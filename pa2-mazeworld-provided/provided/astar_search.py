# julian
# fall 2025
# cosc 76 pa2

from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        return self.transition_cost + self.heuristic

    def __lt__(self, other):
        return self.priority() < other.priority()


def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent
    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[start_node.state] = 0

    while pqueue:
        current_node = heappop(pqueue)
        solution.nodes_visited += 1

        if search_problem.goal_test(current_node.state):
            solution.path = backchain(current_node)
            solution.cost = current_node.transition_cost
            return solution

        for successor_state in search_problem.get_successors(current_node.state):
            new_cost = current_node.transition_cost + 1

            if successor_state not in visited_cost or new_cost < visited_cost[successor_state]:
                visited_cost[successor_state] = new_cost
                heuristic_value = heuristic_fn(successor_state)
                successor_node = AstarNode(successor_state, heuristic_value, current_node, new_cost)
                heappush(pqueue, successor_node)

    return solution
