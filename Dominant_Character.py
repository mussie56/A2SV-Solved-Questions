n = int(input())
for _ in range(n):
    m = int(input())
    s = input()
    
    if "aa" in s:
        print(2)
        continue
    
    minn = float('inf')
    
    for i in range(0,m):
        counta,countb,countc = 0,0,0
        for j in range(i,min(m,i+7)):
            if s[j] == 'a':
                counta+=1
            elif s[j] == 'b':
                countb+=1
            else:
                countc+=1
            
            if j-i > 1:
                if counta > countb and counta > countc:
                    minn = min(minn,j-i+1)
                    
    if minn != float('inf'):
        print(minn)
    else:
        print(-1)
