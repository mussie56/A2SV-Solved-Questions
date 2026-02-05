class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path = []

        for p in paths:
            temp = p.split(" ")
            for i in range(1,len(temp)):
                temp[i] = temp[0]+"/"+temp[i]
                path.append(temp[i])

        res = defaultdict(list)
        
        for p in path:
            key_val = p.split("(")
            if key_val[1] in res:
                res[key_val[1]] = res.get(key_val[1]) + [key_val[0]]
            else:
                res[key_val[1]] = [key_val[0]]

        return [val for val in res.values() if len(val) > 1]
