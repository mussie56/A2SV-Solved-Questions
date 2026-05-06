class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for i in range(n)]
        count = [0 for i in range(n)]
        graph = defaultdict(list)
        for i,j in edges:
            graph[j].append(i)
            count[i]+=1
        
        def dfs(node):
            temp = []
            for i in graph[node]:
                temp+=dfs(i)
            
            ans[node] = temp
            return temp+[node]
        
        for i in range(n):
            if count[i] == 0:
                dfs(i)

        for i in range(n):
            ans[i] = set(ans[i])
            ans[i] = list(ans[i])
            ans[i] = sorted(ans[i])

        return ans