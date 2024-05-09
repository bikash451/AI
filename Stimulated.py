import random
import copy
import math

T = 500

def heuristic(sol):
    a, b, c, d = sol
    f = [[not a or d], [c or b], [not c or not d], [not d or not b], [not a or not d]]
    F = f[0][0] and f[1][0] and f[2][0] and f[3][0] and f[4][0]
    
    c = 0
    for i in range(len(f)):
        if f[i][0] == True:
            c += 1
            
    return c

def movegen(parent):
    random_index = random.randint(0, 3)
    child = copy.deepcopy(parent)
    if parent[random_index] == 1:
        child[random_index] = 0
    else:
        child[random_index] = 1
    return child

def sigmoid_with_temp(delta_e):
    global T 
    prob = 1 / (1 + math.exp(-delta_e) / T)
    return prob

def calculate_delta_e(parent, child):
    delta_e = float(heuristic(child) - heuristic(parent))
    return delta_e

def sampling(prob):
    ans = random.uniform(0, 1)
    if ans >= prob:
        return 1
    else:
        return 0
    
def search(initial_sol, f, F):
    global T
    parent = initial_sol
    curr_max = heuristic(initial_sol)
    count = 0
    sol_list = []
    while count < 100:
        m = 0
        print("Parent:", parent)
        while m < 5:
            child = movegen(parent)
            delta_e = calculate_delta_e(parent, child) 
            
            if delta_e >= 0:
                break
            
            prob = sigmoid_with_temp(delta_e)
            ans = sampling(prob)
            
            print("Child:", child, "Delta E:", delta_e, "Probability:", prob, "Sampled Ans:", ans)
            
            if ans == 1:
                break
                
            m += 1
                  
        if heuristic(child) == 5:
            if child not in sol_list:
                sol_list.append(child)
                  
        if heuristic(child) > curr_max:
            optimal_child = child
            curr_max = heuristic(child)
        parent = child
          
        a, b, c, d = parent
          
        T = T - 50
        if T <= 0:
            T = 1
              
        count += 1
            
    if len(sol_list) == 0:
        print("optimal sol:", optimal_child)
    else:
        print("solutions are:", sol_list)
                  
def main():
    initial_sol = [1, 1, 1, 1]
    a, b, c, d = initial_sol
    f = [[not a or d], [c or b], [not c or not d], [not d or not b], [not a or not d]]
    F = f[0][0] and f[1][0] and f[2][0] and f[3][0] and f[4][0]
    search(initial_sol, f, F)
      
if __name__ == "__main__":
    main()
