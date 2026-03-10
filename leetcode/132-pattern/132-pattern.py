class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        inc = []
        sec = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            while inc and inc[-1] < nums[i]:
                sec = inc.pop()
            inc.append(nums[i])

            if sec > inc[-1]:
                return True 
        return False