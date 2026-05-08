class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.nums = [nums[i] for i in range(min(k,len(nums)))]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        elif len(self.nums) < self.k:
            return
        return self.nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)