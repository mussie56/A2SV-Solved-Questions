class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxx = deque()
        minn = deque()
        j,count = 0,0
        for i in range(len(nums)):
            while maxx and nums[maxx[-1]] < nums[i]:
                maxx.pop()
            while minn and nums[minn[-1]] > nums[i]:
                minn.pop()
            maxx.append(i)
            minn.append(i)
            while nums[maxx[0]] - nums[minn[0]] > limit:
                if maxx[0] == j:
                    maxx.popleft()
                if minn[0] == j:
                    minn.popleft()
                j+=1

            count = max(count,i-j+1)
        return count