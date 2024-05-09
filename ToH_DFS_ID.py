import copy
g = [[],[],['C','B','A']]
q = []
visited = []

def cmp(s,g):
    return s==g

def generate_child_DFS(s):
    global q
    global visited
    for i in range(len(s)):
        temp = copy.deepcopy(s)
        if(s[i]!=[]):
            x = temp[i][-1]
            del temp[i][-1]
            for j in range(len(s)):
                if i!=j:
                    newState = copy.deepcopy(temp)
                    newState[j] = newState[j] + [x]
                    if(newState not in q and newState not in visited):
                        q.insert(0,newState) 

def solve(s):
    global g
    global q
    global visited
    c = 0
    for i in range(1):
        q = []
        q.append(s)
        for j in range(i):
            while len(q):
                cur = q[0]
                del q[0]
                print(cur)
                c = c + 1
                if(cmp(cur,g)):
                    print(f"Found in {c} steps")
                    print(cur)
                    exit()
                generate_child_DFS(cur)
                visited.append(cur)
    print("Not Found")
    exit()


def main():
    global q
    s = [['A'], ['B','C'], []]

    q.append(s)
    solve(s)

if __name__=='__main__':
    main()