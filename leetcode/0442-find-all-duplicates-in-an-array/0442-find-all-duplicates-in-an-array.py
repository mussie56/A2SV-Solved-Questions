class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = set()
        ans = []
        for i in nums:
            if i in dup:
                ans.append(i)
            dup.add(i)
        return ans