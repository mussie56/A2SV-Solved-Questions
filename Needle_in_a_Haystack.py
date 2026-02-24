from collections import defaultdict
for _ in range(int(input())):
    s = list(input())
    t = sorted(list(input()))
    imp = False
    maps = defaultdict(int)
    mapt = defaultdict(int)
    for i in s:
        maps[i]+=1
        
    for i in t:
        mapt[i]+=1
       
    for i in maps:
        if maps[i] > mapt[i]:
            print("Impossible")
            imp = True
            break
        
    if imp:
        continue
    
    j = 0
    ans = []
    for i in mapt:
        
        while j < len(s) and s[j] <= i:
            ans.append(s[j])
            mapt[s[j]]-=1
            maps[s[j]]-=1
            j+=1
            
        if j < len(s): 
            ans.append(i*(mapt[i]-maps[i]))
        else:
            ans.append(i*mapt[i])
    
    print("".join(ans))
