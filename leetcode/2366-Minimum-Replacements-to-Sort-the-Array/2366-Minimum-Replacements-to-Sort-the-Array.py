class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count,n = 0,0
        nums.reverse()
        i = 0
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                if nums[i] == 1:
                    n = 1
                    count+=nums[i+1]-1
                else:
                    n = nums[i+1]//math.ceil(nums[i+1]/nums[i])
                    if nums[i+1]%nums[i] == 0:
                        n = nums[i]
                    count+=math.ceil(nums[i+1]/nums[i])-1#+int(n!=nums[i])
                nums[i+1] = n
                
        return count