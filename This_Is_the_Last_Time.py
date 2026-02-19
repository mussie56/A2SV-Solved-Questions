for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = []
    for i in range(n):
        temp = list(map(int,input().split()))
        if temp[2] > temp[1] or temp[2] < temp[0]:
            continue
        arr.append(temp)
        
    arr.sort()
    found = False
    for i in range(len(arr)):
        if arr[i][0] > k:
            print(k)
            found = True
            break
        
        k = max(k,arr[i][2])
        
    if not found:
        print(k)
