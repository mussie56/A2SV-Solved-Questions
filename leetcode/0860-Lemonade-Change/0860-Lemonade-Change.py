class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mapp = {}
        for i in bills:
            k = i
            while i > 5:
                if i//2 not in mapp:
                    if i//4 not in mapp or mapp[i//4] < 3:
                        return False
                    mapp[i//4]-=3
                    if mapp[i//4] == 0:
                        del mapp[i//4]
                    i//=2
                else:
                    mapp[i//2] -= 1
                    if not mapp[i//2]:
                        del mapp[i//2]
                i//=2
            mapp[k] = mapp.get(k,0)+1
        return True