class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        maxx = 0
        for n in num:
            count = 0
            if n-1 not in num:
                current = n
                count = 1
                while n+1 in num:
                    count+=1
                    n+=1
            maxx = max(maxx,count)

        return maxx
