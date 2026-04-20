class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        cp = [[nums[i],i] for i in range(len(nums))]
        def helper(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2
            left = helper(arr[:mid])
            right = helper(arr[mid:])
            merged = []
            l,r = 0,0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    ans[left[l][1]]+=r
                    merged.append(left[l])
                    l+=1
                else:
                    merged.append(right[r])
                    r+=1
            if r < len(right):
                merged+=right[r:]
            while l < len(left):
                ans[left[l][1]]+=len(right)
                merged.append(left[l])
                l+=1
            return merged

        helper(cp)
        return ans