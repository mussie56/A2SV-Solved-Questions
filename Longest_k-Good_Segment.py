from collections import defaultdict
n,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = []
uni = defaultdict(int)
j,maxx = 0,0
for i in range(n):
    uni[arr[i]]+=1
    
    while len(uni) > k:
        uni[arr[j]] -=1
        if uni[arr[j]] == 0:
            del uni[arr[j]]
        j+=1
    
    if maxx < i-j+1:
        ans = [j+1,i+1]
        maxx = i-j+1
    
print(*ans)
