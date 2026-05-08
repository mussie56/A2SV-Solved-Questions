class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for i in range(n)]
        count = [0 for i in range(n)]
        graph = defaultdict(list)
        for i,j in edges:
            graph[j].append(i)
            count[i]+=1
        
        def dfs(node):
            if ans[node]:
                return [node]+ans[node]
            temp = []
            for i in graph[node]:
                temp+=dfs(i)
            temp = set(temp)
            temp = list(temp)
            ans[node] = sorted(temp)
            return temp+[node]
        
        for i in range(n):
            if count[i] == 0:
                dfs(i)

        return ans