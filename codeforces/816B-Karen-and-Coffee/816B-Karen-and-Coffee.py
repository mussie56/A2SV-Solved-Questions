n,k,q = map(int,input().split())
arr = []
minn,maxx = float('inf'),0

for _ in range(n):
    a,b = map(int,input().split())
    minn = min(minn,a,b)
    maxx = max(maxx,a,b)
    arr.append([a,b])
quest = []
for _ in range(q):
    a,b = map(int,input().split())
    minn = min(minn,a,b)
    maxx = max(maxx,a,b)
    quest.append([a,b])
    
pref = [0]*(maxx-minn+2)

for l,r in arr:
    l-=minn
    r-=minn
    pref[l] += 1
    pref[r+1] -= 1
    
for i in range(1,len(pref)):
    pref[i] += pref[i-1]

for i in range(len(pref)):
    pref[i] = 1 if pref[i] >= k else 0
    if i > 0:
        pref[i] += pref[i-1]

pref[-1] = 0

for l,r in quest:
    l -= minn
    r -= minn
    print(pref[r]-pref[l-1])