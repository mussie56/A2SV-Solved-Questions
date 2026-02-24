class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l,r = 1,len(skill)-2
        skill.sort()
        skills = skill[0]+skill[-1]
        chem = skill[0]*skill[-1]
        
        while l < r:
            if skill[l]+skill[r] != skills:
                return -1

            chem+=skill[l]*skill[r]
            r-=1
            l+=1

        return chem
