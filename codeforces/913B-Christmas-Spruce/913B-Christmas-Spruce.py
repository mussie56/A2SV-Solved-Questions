from collections import Counter
n = int(input())
arr = []
for _ in range(n-1):
    arr.append(int(input()))

mapp = Counter(arr)

m = 2
for i in arr:
    if m in mapp:
        mapp[i]-=1
    m+=1
 
for i in mapp:
    if mapp[i] < 3:
        print("No")
        exit()
print("Yes")