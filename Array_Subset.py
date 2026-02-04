class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        a.sort()
        b.sort()
        c = 0
        j = 0
        for i in range(len(b)):
            while j < len(a):
                if b[i] == a[j]:
                    j+=1
                    c+=1
                    break
                j+=1
        return c == len(b)
