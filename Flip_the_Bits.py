for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    b = input().strip()
    
    balance = 0
    prefix_balanced = [False]*n
    
    for i in range(n):
        if a[i] == '1':
            balance += 1
        else:
            balance -= 1    
        if balance == 0:
            prefix_balanced[i] = True
    
    flip = False
    possible = True
    
    for i in range(n-1, -1, -1):
        current = a[i]
        
        if flip:
            current = '1' if current == '0' else '0'
        
        if current != b[i]:
            if not prefix_balanced[i]:
                possible = False
                break
            flip = not flip
    
    print("YES" if possible else "NO")
