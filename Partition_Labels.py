class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapp = Counter(s)
        ans = []
        original = len(mapp)
        ss = set()
        count = 0
        for i in s:
            if i in mapp:
                count +=1
                ss.add(i)
                mapp[i]-=1
                if mapp[i] == 0:
                    del mapp[i]
            if len(ss) == original-len(mapp):
                if count:
                    ans.append(count)
                    count = 0
                    ss.clear()
                    original = len(mapp)
                    
        return ans
