from collections import defaultdict,Counter
for _ in range(int(input())):
    s = input()
    mapd = defaultdict(int)
    mapp = Counter(s)
    i = 0
    while i < len(s)-1:
        mapd[s[i]+s[i+1]] += 1
        if s[i] == s[i+1]:
            i+=2
        else:
            i+=1
    
    res = []
    for i in mapp:
        if i*2 in mapd and mapd[i*2]*2 == mapp[i]:
            continue
        else:
            res.append(i)
            
    res.sort()
    
    print("".join(res))
