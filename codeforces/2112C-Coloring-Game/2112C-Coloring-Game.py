for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    count = 0
    total = n*(n-1)*(n-2)//6
    for i in range(n-1,1,-1):
        j,k = i-1,0
        while j > k:
            if arr[k]+arr[j] > arr[i] and arr[k]+arr[j]+arr[i] > arr[-1]:
                j-=1
            else:
                count+=(j-k)
                k+=1
                
    print(total-count)