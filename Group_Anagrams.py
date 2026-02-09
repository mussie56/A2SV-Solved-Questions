class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if d.get(s) == None:
                d[s] = [strs[i]]
            else:
                d[s].append(strs[i])
        return [val for val in d.values()]
