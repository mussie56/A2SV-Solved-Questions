from collections import defaultdict
arr =[]
order = []
alpha = "abcdefghijklmnopqrstuvwxyz"
n = int(input())
for _ in range(n):
    arr.append(input())
    
graph = defaultdict(list)   
graph[arr[0][0]] = []

for i in range(1,n):
    j = 0
    maxx = min(len(arr[i]),len(arr[i-1]))
    while j < maxx and arr[i][j] == arr[i-1][j]:
        j+=1
    if j < maxx:
        graph[arr[i][j]].append(arr[i-1][j])
        graph[arr[i-1][j]]+=[]
        # graph[arr[i][j]] += graph[arr[i-1][j]]
    else:
        if j < len(arr[i-1]):
            print("Impossible")
            exit()
    
# print(graph)
    
color = {i:0 for i in graph}

def dfs(node):
    if color[node] == 1:
        return False
    color[node] = 1
    for i in graph[node]:
        if color[i] == 2:
            continue
        if not dfs(i):
            return False
    color[node] = 2
    order.append(node)
    return True

for i in color:
    if color[i] == 0:
        if not dfs(i):
            print("Impossible")
            exit()

for i in alpha:
    if i not in order:
        order.append(i)

print("".join(order))