class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vertex = {}
        for i in range(len(graph)):
            vertex[i] = graph[i]
        mapp = {i:-1 for i in vertex}
        nope = False
        visited = set()
        def dfs(node,color):
            nonlocal nope
            if nope:
                return
            visited.add(node)
            mapp[node] = color
            for i in vertex[node]:
                if i not in visited:
                    dfs(i,(color+1)%2)
                else:
                    if mapp[i] == mapp[node]:
                        nope = True
                        break

        for i in vertex:
            if nope:
                break
            if i not in visited:
                dfs(i,0)    #colors 0 and 1
        return not nope