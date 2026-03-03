for _ in range(int(input())):
    n = int(input())
    r = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    prefr = [0]
    prefb = [0]
    for i in r:
        prefr.append(prefr[-1]+i)
    for i in b:
        prefb.append(prefb[-1]+i)
        
    print(max(prefr)+max(prefb))