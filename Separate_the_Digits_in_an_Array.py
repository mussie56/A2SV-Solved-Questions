class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            s = str(i)
            for j in s:
                ans.append(int(j))

        return ans
