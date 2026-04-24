from collections import defaultdict,deque

def maxDistance(node,n,graph):  #returns the maximum distance and the node on that distance
    dist = [-1]*(n+1)
    que = deque([node])
    dist[node] = 0
    far = node
    while que:
        curr = que.popleft()
        for i in graph[curr]:
            if dist[i] == -1:
                que.append(i)
                dist[i] = dist[curr]+1
            if dist[i] > dist[far]:
                far = i
    return [dist[far],far]

n = int(input())
if n == 1:
    print(0)
    exit()

graph = defaultdict(list)
for i in range(n-1):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

_,temp = maxDistance(1,n,graph)
maxx,node = maxDistance(temp,n,graph)

print(maxx*3)