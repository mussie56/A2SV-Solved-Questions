for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    if "B"*k in s:
        print(0)
        continue
    
    count = 0
    for i in range(k):
        if s[i] == "B":
            count+=1
    minn = k-count
    for i in range(k,n):
        if s[i] == "B":
            count+=1
        if s[i-k] == "B":
            count -= 1
        
        minn = min(minn,k-count)
        
    print(minn)
