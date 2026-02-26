class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapp = defaultdict(int)
        j = 0
        maxx,max_Count = 0,0
        for i in range(len(s)):
            mapp[s[i]]+=1
            max_Count = max(max_Count,mapp[s[i]])

            while max_Count + k < i-j+1:
                mapp[s[j]]-=1
                if mapp[s[j]] == 0:
                    del mapp[s[j]]
                j+=1
              
            maxx = max(maxx,i-j+1)
        return maxx
