from collections import deque

# Function to find all possible states from the current state
def generate_states(state, path):
    a, b = state
    next_states = []
    # Fill jug A
    next_state = (4, b)
    if next_state not in path:
        next_states.append(next_state)
    # Fill jug B
    next_state = (a, 3)
    if next_state not in path:
        next_states.append(next_state)
    # Empty jug A
    next_state = (0, b)
    if next_state not in path:
        next_states.append(next_state)
    # Empty jug B
    next_state = (a, 0)
    if next_state not in path:
        next_states.append(next_state)
    # Pour from A to B
    transfer_amount = min(a, 3 - b)
    next_state = (a - transfer_amount, b + transfer_amount)
    if next_state not in path:
        next_states.append(next_state)
    # Pour from B to A
    transfer_amount = min(4 - a, b)
    next_state = (a + transfer_amount, b - transfer_amount)
    if next_state not in path:
        next_states.append(next_state)
        
    return next_states

def bfs(start_state, goal):
    queue = deque([(start_state, [start_state])])
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path
        next_states = generate_states(current_state, path)
        for next_state in next_states:
            queue.append((next_state, path + [next_state]))
    return None

start_state = (0, 0)
goal_state = (2, 0)


path = bfs(start_state, goal_state)


if path:
    print("Solution found!")
    for state in path:
        print(state)
else:
    print("No solution exists.")