import math
a = int(input())
b = int(input())
m = int(input())

print(int(math.pow(a,b)))

if b >= 0:
    print(int(math.pow(a,b)%m))
