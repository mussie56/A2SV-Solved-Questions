class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dom = Counter(nums)
        dom_num = 0
        val = max(dom.values())
        
        for i in dom:
            if dom[i] == val:
                dom_num = i
                break
                
        index = -1
        
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == dom_num:
                count+=1
            
            if count > (i+1)//2:
                break
            i+=1
        index = i
        count1 = 0
        i+=1
        while i < len(nums):
            if nums[i] == dom_num:
                count1+=1
            i+=1

        if count1 > (len(nums)-index-1)//2:
            return index
        return -1
