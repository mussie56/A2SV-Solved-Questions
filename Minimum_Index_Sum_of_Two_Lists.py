class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash1 = {}
        for l in range(len(list1)):
            hash1[list1[l]] = l
        res = {}
        minn = float('inf')
        for l in range(len(list2)):
            if list2[l] in hash1:
                res[list2[l]] = hash1.get(list2[l]) + l
                minn = min(minn,res[list2[l]])
        
        return [key for key,val in res.items() if val == minn]
