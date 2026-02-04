class Solution:    
    def findUnion(self, a, b):
        # code here
        union = set()
        for i in a:
            union.add(i)
        for i in b:
            union.add(i)
        return list(union)
