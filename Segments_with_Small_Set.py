from collections import defaultdict
n,k = map(int,input().split())
arr = list(map(int,input().split()))
visited = defaultdict(int)
count,j = 0,0
for i in range(n):
    visited[arr[i]] += 1
    
    while len(visited) > k:
        visited[arr[j]] -=1
        if visited[arr[j]] == 0:
            del visited[arr[j]]
        j+=1
    
    count+=(i-j+1)
    
print(count)
