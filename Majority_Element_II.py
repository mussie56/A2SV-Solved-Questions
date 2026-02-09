class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = {}
        for i in nums:
            majority[i] = majority.get(i,0)+1
        return [key for key,val in majority.items() if val >len(nums)//3]
