class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        changed.sort()
        mapp = Counter(changed)
        for i in changed:
            if i == 0:
                continue
            if i in mapp:
                if i*2 in mapp:
                    ans.append(i)
                    mapp[i] -=1
                    mapp[i*2] -= 1
                    if mapp[i] == 0:
                        del mapp[i]
                    if mapp[i*2] == 0:
                        del mapp[i*2]
                        
        if 0 in mapp and mapp[0]%2==0:
            for i in range(mapp[0]//2):
                ans.append(0)

        if len(ans) == len(changed)/2:
            return ans
        return []
