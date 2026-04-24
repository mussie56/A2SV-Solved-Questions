for _ in range(int(input())):
    n = int(input())
    edge = []
    for i in range(n):
        s = input()
        s = list(s)
        edge.append(s)
    ans = [1]
    for i in range(2,n+1):
        j = 0
        while j < len(ans) and edge[ans[j]-1][i-1] == '1' or i == j:
            j+=1
        if j == len(ans):
            ans.append(i)
            continue
        ans.insert(j,i)
    print(*ans)