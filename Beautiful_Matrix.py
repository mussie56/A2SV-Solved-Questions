arr = []
for _ in range(5):
    temp = list(map(int,input().split()))
    arr.append(temp)
    
col = 0
row = 0
found = False
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            col = j
            row = i
            found = True
            break
    if found:
        break
    
print(abs(col-2)+abs(row-2))
