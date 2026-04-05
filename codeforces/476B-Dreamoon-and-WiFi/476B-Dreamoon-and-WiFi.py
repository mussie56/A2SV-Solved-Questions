from collections import Counter
from decimal import Decimal,getcontext
def outer():
    getcontext().prec = 10
    original = input()
    maporig = Counter(original)
    received = input()
    mapr = Counter(received)
    total = 2**mapr['?']
    goal = maporig['+']-maporig['-']
    count = 0
    n = len(original)
    def backtrack(i,summ):
        nonlocal n
        nonlocal count
        if i > n:
            return
        if i == n:
            if summ == goal:
                count+=1
            return
        
        if received[i] == '+':
            backtrack(i+1,summ+1)
        elif received[i] == '-':
            backtrack(i+1,summ-1)
        else:
            backtrack(i+1,summ+1)
            backtrack(i+1,summ-1)
        
    backtrack(0,0)
    ans = Decimal(str(1)) if mapr['+']-mapr['-']==goal else Decimal(str(0))
    print(Decimal(str(count))/Decimal(str(total)) if total > 0 else ans)

outer()