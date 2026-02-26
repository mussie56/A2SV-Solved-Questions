from collections import Counter
n,m = map(int,input().split())
map1 = Counter(map(int,input().split()))
map2 = Counter(map(int,input().split()))
count = 0
for i in map2:
    if i in map1:
        count+=map1[i]*map2[i]

print(count)
