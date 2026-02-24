for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    k = 0
    ans = []
    visited = set()
    while k < n-1:
        j,i = k,k+1
        while i < n and arr[i] < arr[j]:
            i+=1
            j+=1
            
        if k not in visited:
            ans.append(arr[k])
            visited.add(k)
        k = j
        
        while i < n and arr[i] > arr[j]:
            i+=1   
            j+=1
        
        if k not in visited:
            ans.append(arr[k])
            visited.add(k)
        k = j    
    
    if k not in visited:
            ans.append(arr[k])
            
    print(len(ans)) 
    print(*ans)
