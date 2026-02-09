class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            count[i] = count.get(i,0)+1

        for k,v in count.items():
            if v == 1:
                return k
