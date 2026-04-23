class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        edge = defaultdict(list)
        for i in range(len(graph)):
            edge[i] = graph[i]
        ans = []
        def dfs(node,temp):
            if node == len(graph)-1:
                ans.append(temp[:])
                return
            for i in edge[node]:
                temp.append(i)
                dfs(i,temp)
                temp.pop()
            
        dfs(0,[0])
        return ans