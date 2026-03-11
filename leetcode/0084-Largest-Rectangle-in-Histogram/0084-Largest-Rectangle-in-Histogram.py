class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxx = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                curr = stack.pop()
                ind = 0
                if stack:
                    ind = stack[-1]+1
                maxx = max(maxx,(i-ind)*heights[curr])
            stack.append(i)

        i = len(heights)

        while stack:
            ind = 0
            curr = stack.pop()
            if stack:
                ind = stack[-1]+1
            maxx = max(maxx,(i-ind)*heights[curr])
        return maxx