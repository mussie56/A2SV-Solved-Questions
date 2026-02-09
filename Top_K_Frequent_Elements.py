class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = {}
        for i in nums:
            num[i] = num.get(i,0)+1

        num = list(num.items())
        num.sort(key=lambda x:x[1], reverse=True)
        
        return [num[i][0] for i in range(k)]
