class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def withinRange(center,point):
            d = math.sqrt(((center[0]-point[0])**2)+((center[1]-point[1])**2))
            return d <= center[2]
        counts = defaultdict(int)
        sub = {tuple(b):[] for b in bombs}
        for i in range(len(bombs)):
            counts[tuple(bombs[i])] += 1
            for j in range(len(bombs)):
                if i == j:
                    continue
                if withinRange(bombs[i],bombs[j]): # bomb with in the range of the ith bomb
                    sub[tuple(bombs[i])].append(tuple(bombs[j]))
        print(sub)           
        visited = set()
        
        def dfs(node):
            count = counts[node]
            for i in sub[node]:
                if i not in visited:
                    visited.add(i)
                    count+=dfs(i)
            return count

        maxx = 0
        for i in sub:
            visited = set([i])
            res = dfs(i)
            maxx = max(maxx,res)
        return maxx