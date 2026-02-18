n = int(input())
arr = list(map(int,input().split()))
ans = []
arr.sort()
add = 0
for i in range(n):
    if arr[i] >= i-add+1:
        ans.append(arr[i])
    else:
        add+=1
print(len(ans))
