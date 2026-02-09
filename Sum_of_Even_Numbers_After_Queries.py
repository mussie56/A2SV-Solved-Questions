class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        summ = 0
        for i in nums:
            if i%2 == 0:
                summ+=i
                
        for val,ind in queries:
            if nums[ind]%2 == 0:
                if val%2 == 0:
                    summ+=val
                else:
                    summ-=nums[ind]
            else:
                if val%2==1:
                    summ+=nums[ind]+val

            nums[ind] = nums[ind] + val
            
            ans.append(summ)

        return ans
