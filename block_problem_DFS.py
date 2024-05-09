def blocks_world_dfs(initial_state, goal_state):
    visited_states = set()
    stack = [(initial_state, [])]

    while stack:
        current_state, actions = stack.pop()
        print("Current State:", current_state)
        if current_state == goal_state:
            return actions
        if tuple(current_state) in visited_states:
            continue
        visited_states.add(tuple(current_state))
        possible_actions = generate_actions(current_state)
        for action in possible_actions:
            new_state = apply_action(current_state, action)
            stack.append((new_state, actions + [action]))

    return None

def generate_actions(state):
    actions = []
    for block in state:
        actions.append(("move", block))
        actions.append(("stack", block))
    return actions

def apply_action(state, action):
    action_type, block = action
    new_state = state[:]
    if action_type == "move":
        new_state.remove(block)
        new_state.insert(0, block) 
    elif action_type == "stack":
        new_state.remove(block)
        new_state.append(block)
    return new_state

initial_state = ['A', 'C', 'B']
goal_state = ['A', 'B', 'C']

solution = blocks_world_dfs(initial_state, goal_state)
print("Solution:", solution)