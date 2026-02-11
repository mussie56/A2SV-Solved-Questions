class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = {}
        removed = []

        for i in range(len(responses)):
            removed.append(list(set(responses[i])))

        for i in range(len(removed)):
            for j in range(len(removed[i])):
                count[removed[i][j]] = count.get(removed[i][j], 0)+1

        count = list(count.items())
        count.sort()
        count.sort(key=lambda x:-x[1])
        
        return count[0][0]
