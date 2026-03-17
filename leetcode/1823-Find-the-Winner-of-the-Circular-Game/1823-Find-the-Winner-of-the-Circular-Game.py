class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(nums: List[int],k: int,ind: int) -> int:
            if len(nums) == 1:
                return nums[0]
            i = (k-1+ind)%len(nums)
            ind = i
            while i < len(nums)-1:
                nums[i] = nums[i+1]
                i+=1
            nums.pop()
            return helper(nums,k,ind)

        nums = []
        for i in range(n):
            nums.append(i+1)
        return helper(nums,k,0)