class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        c = []
        for m in range(2):
            unique = defaultdict(int)
            count,j = 0,0
            for i in range(len(nums)):
                unique[nums[i]] += 1

                while len(unique) > k-m:
                    unique[nums[j]] -= 1
                    if unique[nums[j]] == 0:
                        del unique[nums[j]]
                    j+=1

                count+=i-j+1
            c.append(count)

        return c[0]-c[1]
