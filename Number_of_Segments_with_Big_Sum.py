n,s = map(int,input().split())
arr = list(map(int,input().split()))
count,summ,j = 0,0,0
for i in range(n):
    summ+=arr[i]
    while summ >= s:
        count+=(n-i)
        summ-=arr[j]
        j+=1
        
print(count)
