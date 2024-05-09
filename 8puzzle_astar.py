from queue import PriorityQueue

def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def heuristic(state):
    count = 0
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                count += 1
    return count

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

def path_cost(state):
    # Path cost is the number of moves taken to reach the current state
    cost = 0
    while state != initial_state:
        state = parent[state]
        cost += 1
    return cost

def astar(start):
    # Define a function to calculate the total cost for A* (heuristic + path cost)
    def total_cost(state):
        return heuristic(state) + path_cost(state)

    # Priority queue for the frontier
    frontier = PriorityQueue()
    frontier.put((total_cost(start), start))
    explored = set()  # To keep track of explored states

    while not frontier.empty():
        _, current_state = frontier.get()  # Get the state with the lowest total cost
        current_state_tuple = tuple(map(tuple, current_state))  # Convert to tuple for hashability
        if current_state_tuple in explored:
            continue

        explored.add(current_state_tuple)

        if is_goal(current_state):  # Check if current_state is goal state
            return current_state

        for move in generate_moves(current_state):
            move_cost = path_cost(current_state) + 1  # Assuming uniform cost
            move_tuple = tuple(map(tuple, move))  # Convert to tuple for hashability
            if move_tuple not in explored:
                parent[move_tuple] = current_state_tuple  # Update parent for the move
                frontier.put((total_cost(move), move))

    return None  # No solution found

# Replace path_cost with appropriate cost calculation function
initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
parent = {tuple(map(tuple, initial_state)): None}  # To keep track of parent states
solution = astar(initial_state)
if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution found.")
