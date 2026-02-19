n,k = map(int,input().split())
if k == n:
    print(0)
    exit()
arr = list(map(int,input().split()))
diff = []

for i in range(n-1):
    diff.append(arr[i+1]-arr[i])

diff.sort(reverse = True)

print(sum(diff[k-1:]))
