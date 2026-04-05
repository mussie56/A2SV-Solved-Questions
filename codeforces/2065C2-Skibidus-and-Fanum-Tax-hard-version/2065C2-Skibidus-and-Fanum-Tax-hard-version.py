def findmax(curr,maxx,b):
    ans = float('inf')
    l,r = 0,len(b)-1
    while l<=r:
        mid = (l+r)//2
        if b[mid]-curr <= maxx:
            ans = b[mid]-curr
            l = mid+1
        else:
            r = mid-1
    return ans

for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()
    nope = False
    a[-1] = max(a[-1],b[-1]-a[-1])
    for i in range(n-2,-1,-1):
        temp =  findmax(a[i],a[i+1],b)
        if temp == float('inf') and a[i] > a[i+1]:
            nope = True
            break
        if temp==float('inf'):
            temp = a[i]
        if a[i] <= a[i+1]:
            temp = max(temp,a[i])
        a[i] = temp      
    print("YES" if not nope else "NO")