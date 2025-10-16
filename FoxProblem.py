# cosc 76 pa1 julian 2025
class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.total_chickens = start_state[0]
        self.total_foxes = start_state[1]

    def get_successors(self, state):
        successors = []
        chickens, foxes, boat = state
        
        # boat on starting side move animals to other side
        if boat == 1:
            for c in range(min(3, chickens + 1)):
                for f in range(min(3, foxes + 1)):
                    if 1 <= c + f <= 2:
                        new_state = (chickens - c, foxes - f, 0)
                        if self.is_legal(new_state):
                            successors.append(new_state)
        else:  # boat on other side bring animals back
            other_chickens = self.total_chickens - chickens
            other_foxes = self.total_foxes - foxes
            for c in range(min(3, other_chickens + 1)):
                for f in range(min(3, other_foxes + 1)):
                    if 1 <= c + f <= 2:
                        new_state = (chickens + c, foxes + f, 1)
                        if self.is_legal(new_state):
                            successors.append(new_state)
        
        return successors
    
    def is_legal(self, state):
        # check if chickens get eaten
        chickens, foxes, boat = state
        other_chickens = self.total_chickens - chickens
        other_foxes = self.total_foxes - foxes
        
        if chickens < 0 or foxes < 0 or other_chickens < 0 or other_foxes < 0:
            return False
        
        if chickens > 0 and foxes > chickens:
            return False
        
        if other_chickens > 0 and other_foxes > other_chickens:
            return False
        
        return True
    
    def goal_test(self, state):
        return state == self.goal_state

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string



if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
