for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    res = []
    count = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                count+=1
                a[j],a[j+1] = a[j+1],a[j]
                res.append([1,j+1])
            
    for i in range(n-1):
        for j in range(n-i-1):
            if b[j] > b[j+1]:
                count+=1
                b[j],b[j+1] = b[j+1],b[j]
                res.append([2,j+1])
                
    for i in range(n):
        if a[i] > b[i]:
            a[i],b[i] = b[i],a[i]
            count +=1
            res.append([3,i+1])
            
    print(count)
    for i in range(count):
        print(res[i][0],res[i][1])
