from queue import PriorityQueue

def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def is_goal(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def generate_moves(state):
    moves = []
    row, col = find_blank(state)
    if row > 0:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
        moves.append(new_state)
    if row < 2:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
        moves.append(new_state)
    if col > 0:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
        moves.append(new_state)
    if col < 2:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]
        moves.append(new_state)
    
    return moves

def heuristic(state):
    goal=[[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=goal[i][j]:
                count +=1
    return count

def best_first_search(start):
    visited = set()
    queue = PriorityQueue()
    queue.put((heuristic(start), start))  
    while not queue.empty():
        _, state = queue.get()
        visited.add(str(state))        
        if is_goal(state):
            return state       
        print("Intermediate state:")
        for row in state:
            print(row)
        print()       
        for move in generate_moves(state):
            if str(move) not in visited:
                queue.put((heuristic(move), move))               
    return None

initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
solution = best_first_search(initial_state)
if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution exists.")