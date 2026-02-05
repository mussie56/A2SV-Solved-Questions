class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        return [key for key,val in count.items() if val == 2]
