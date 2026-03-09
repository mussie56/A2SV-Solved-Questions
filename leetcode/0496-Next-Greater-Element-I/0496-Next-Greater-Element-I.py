class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*(max(nums2)+1)
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack:
                ans[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        res = []
        for i in  nums1:
            res.append(ans[i])
        
        return res