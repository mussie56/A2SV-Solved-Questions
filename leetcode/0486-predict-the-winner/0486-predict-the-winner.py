class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def helper(l: int,r: int) -> int:
            if l == r:
                return nums[l]
            pl = nums[l] - helper(l+1,r)
            pr = nums[r] - helper(l,r-1)

            return max(pl,pr)

        return helper(0,len(nums)-1) >= 0