import copy

q = []
seen = set()
g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
s = [[2, 8, 3], [1, 5, 4], [7, 6, 0]]    

def dist(s):
    x = 0
    global g
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != g[i][j]:
                x += 1
    return x

def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i, j]
 
def up(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if x > 0:
        s1[x][y] = s1[x - 1][y]
        s1[x - 1][y] = 0
        return s1
    else:
        return None
 
def down(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if x < 2:
        s1[x][y] = s1[x + 1][y]
        s1[x + 1][y] = 0
        return s1
    else:
        return None
 
def left(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if y > 0:
        s1[x][y] = s1[x][y - 1]
        s1[x][y - 1] = 0
        return s1
    else:
        return None
 
def right(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if y < 2:
        s1[x][y] = s1[x][y + 1]
        s1[x][y + 1] = 0
        return s1
    else:
        return None

def generate_child(s):
    global q
    global seen
    
    new_state = up(s)
    if new_state is not None:
        state_tuple = tuple(map(tuple, new_state))
        if state_tuple not in seen:
            q.append(new_state) 
            seen.add(state_tuple)
    
    new_state = down(s)
    if new_state is not None:
        state_tuple = tuple(map(tuple, new_state))
        if state_tuple not in seen:
            q.append(new_state) 
            seen.add(state_tuple)
    
    new_state = left(s)
    if new_state is not None:
        state_tuple = tuple(map(tuple, new_state))
        if state_tuple not in seen:
            q.append(new_state) 
            seen.add(state_tuple)
    
    new_state = right(s)
    if new_state is not None:
        state_tuple = tuple(map(tuple, new_state))
        if state_tuple not in seen:
            q.append(new_state) 
            seen.add(state_tuple)

def search(g):
    global q
    global seen
    global s
    c = 0

    while q:
        print(q)
        current_state = q.pop(0)
        c += 1

        if current_state == g:
            print(f"Found in {c} steps")
            return
        
        generate_child(current_state)
        
    print("Cannot Find Solution")

def main():
    global q
    global g
    global s    
    
    q.append(s)
    seen.add(tuple(map(tuple, s)))
    search(g)
 
if __name__ == "__main__":
    main()
