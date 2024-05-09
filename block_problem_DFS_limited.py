def blocks_world_dls(initial_state, goal_state, depth_limit):
    return dls_recursive(initial_state, goal_state, [], depth_limit)

def dls_recursive(current_state, goal_state, actions, depth_limit):
    if current_state == goal_state:
        return actions
    if depth_limit == 0:
        return None

    possible_actions = generate_actions(current_state)
    for action in possible_actions:
        new_state = apply_action(current_state, action)
        result = dls_recursive(new_state, goal_state, actions + [action], depth_limit - 1)
        if result is not None:
            return result

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

# Example usage:
initial_state = ['A', 'C', 'B']
goal_state = ['A', 'B', 'C']
depth_limit = 5  # You can adjust the depth limit as needed

solution = blocks_world_dls(initial_state, goal_state, depth_limit)
print("Solution:", solution)