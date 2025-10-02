# FoxProblem.py
# julian gutierrez 25f

# state is (chickens_start, foxes_start, boat_start)
# boat_start = 1 means boat is on start side

class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.total_chickens = start_state[0]
        self.total_foxes = start_state[1]

    def get_start_state(self):
        return self.start_state

    def is_goal(self, state):
        return state == (0, 0, 0)

    def is_legal_state(self, state):
        chickens_start, foxes_start, boat_start = state
        chickens_end = self.total_chickens - chickens_start
        foxes_end = self.total_foxes - foxes_start

        # bounds check
        if (chickens_start < 0 or foxes_start < 0 or
            chickens_start > self.total_chickens or foxes_start > self.total_foxes or
            boat_start not in [0, 1]):
            return False

        # foxes cant outnumber chickens
        if chickens_start > 0 and foxes_start > chickens_start:
            return False
        if chickens_end > 0 and foxes_end > chickens_end:
            return False

        return True

    def get_successors(self, state):
        successors = []
        chickens_start, foxes_start, boat_start = state

        # all possible moves
        possible_moves = [
            (1, 0),  # 1 chicken
            (2, 0),  # 2 chickens
            (0, 1),  # 1 fox
            (0, 2),  # 2 foxes
            (1, 1),  # 1 chicken 1 fox
        ]

        for chickens_move, foxes_move in possible_moves:
            if boat_start == 1:  # moving from start to end
                new_chickens_start = chickens_start - chickens_move
                new_foxes_start = foxes_start - foxes_move
                new_boat_start = 0
            else:  # moving from end to start
                new_chickens_start = chickens_start + chickens_move
                new_foxes_start = foxes_start + foxes_move
                new_boat_start = 1

            new_state = (new_chickens_start, new_foxes_start, new_boat_start)

            # check if we have enough animals to move
            if boat_start == 1:
                if chickens_move <= chickens_start and foxes_move <= foxes_start:
                    if self.is_legal_state(new_state):
                        successors.append(new_state)
            else:
                chickens_end = self.total_chickens - chickens_start
                foxes_end = self.total_foxes - foxes_start
                if chickens_move <= chickens_end and foxes_move <= foxes_end:
                    if self.is_legal_state(new_state):
                        successors.append(new_state)

        return successors

    def __str__(self):
        return f"foxes problem: {self.start_state}"