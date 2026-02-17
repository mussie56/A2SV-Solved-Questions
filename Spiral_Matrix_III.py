class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        top,bottom,right,left = rStart,rStart+1,cStart+1,cStart

        while bottom != rows or left != -1 or top != -1 or right!=cols:
            for j in range(max(left, 0),min(cols,right+1)):
                if top > -1:
                    ans.append([top, j])

            for i in range(max(0,top+1),min(bottom+1,rows)):
                if right < cols:
                    ans.append([i, right])

            for j in range(min(right-1,cols-1),max(-1,left-2),-1):
                if bottom < rows:
                    ans.append([bottom, j])

            for i in range(min(bottom-1,rows-1),max(top-1,-1),-1):
                if left > 0:
                    ans.append([i, left-1])

            top = top-1 if top > 0 else -1
            left = left-1 if left > 0 else -1
            bottom = bottom+1 if bottom < rows-1 else rows
            right = right+1 if right < cols-1 else cols

        return ans
