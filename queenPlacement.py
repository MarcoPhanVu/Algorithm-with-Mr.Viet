def place_N_queens_on_MxM_board(N, M):
    solution = list()
    current_state = list()
    
    get_solution(current_state, solution, N, M)
    
    for way in solution:
        print(way)
        pass

def is_valid_state(state, n): # State is valid to check for wrong solutions 
    return len(state) == n
    
def get_available_slot(state, n):
    if len(state) == 0:
        return range(n) # Place any where
    
    # Find next positio n in state to populate
    index = len(state)
    slot = set(range(n)) # set will remove duplicated, equal values
    
    for row, col in enumerate(state):
        # discard whole col, row is dealt with the index count
        slot.discard(col) # use discard to ignore errors raised when no number was there
        dist = index - row
        # discard diagonals
        slot.discard(col + dist) 
        slot.discard(col - dist) 
        
    return slot
    
def get_solution(state, solution, n_queen = 4, m_board_size= 4):
    if (is_valid_state(state, n_queen)):
        solution.append(state.copy())  # .copy() prevent all reference to a single object by creating a new instance when ever it is created.
        return solution
    
    for slot in get_available_slot(state, n_queen):
        state.append(slot)
        get_solution(state, solution, n_queen, m_board_size)
        state.pop()
    
    return solution

place_N_queens_on_MxM_board(4, 4)