class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        head,step = 1,1
        remain = n
        while remain > 1:
            if left or remain%2:
                head+=step
            step *= 2
            remain //= 2
            left = not left
        return head

        # def helper(nums: Lit[int]) -> int:
        #     if len(nums) == 1:
        #         return nums[0]
        #     k = len(nums)
        #     nums.reverse()
        #     i,j = 0,0
        #     while j < k:
        #         if j%2:
        #             nums[i],nums[j] = nums[j],nums[i]
        #             i+=1
        #         j+=1
        #     return helper(nums[:k//2])

        # nums = []
        
        # for i in range(n-1,-1,-1):
        #     nums.append(i+1)
        # return helper(nums)