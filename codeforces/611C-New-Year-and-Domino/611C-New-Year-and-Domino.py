n,m = map(int,input().split())
s = []
for _ in range(n):
    s.append(input())
query = []
q = int(input())
for _ in range(q):
    query.append(list(map(int,input().split())))

pref = [[0 for _ in range(m+1)] for _ in range(n+1)]
mat = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(2,m+1):
        mat[i][j] = 1 if s[i-1][j-2] == "." and s[i-1][j-1] == "." else 0

for i in range(2,n+1):
    for j in range(1,m+1):
        pref[i][j] = 1 if s[i-2][j-1] == "." and s[i-1][j-1] == "." else 0
        
for i in range(1,n+1):
    for j in range(1,m+1):
        mat[i][j] += mat[i][j-1] + mat[i-1][j] - mat[i-1][j-1]
        
for j in range(1,m+1):
    for i in range(1,n+1):
        pref[i][j] += pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]

for r1,c1,r2,c2 in query:
    if r1 == r2 and c1 == c2:
        print(0)
        continue
    
    res = pref[r2][c2]-pref[r2][c1-1]-pref[r1][c2] +pref[r1][c1-1] + mat[r2][c2]-mat[r2][c1] - mat[r1-1][c2] + mat[r1-1][c1]
    
    print(res)