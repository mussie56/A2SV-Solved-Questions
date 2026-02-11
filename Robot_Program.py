for _ in range(int(input())):
    n,x,y = map(int,input().split())
    s = input()
    k = y
    i,count,before = 0,0,0
    visited = False
    while i < n and k > 0:
        if s[i] == 'L':
            x-=1
        else:
            x+=1
            
        k-=1
        i+=1
        
        if x == 0:
            if not visited:
                before = i
                i = 0
                count+=1
                visited = True
                continue
            else:
                count = (y-before)//(i) + 1
                break
        
    print(count)
