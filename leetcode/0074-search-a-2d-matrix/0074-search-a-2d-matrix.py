class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def check(nums,target):
            l,r = 0,len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return False
             
        l,r = 0,len(matrix)-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid-1
            else:
                if check(matrix[mid],target):
                    return True
                l = mid+1
        return False