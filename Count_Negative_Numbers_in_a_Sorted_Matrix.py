class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        for g in grid:
            index = n
            l,r = 0,n-1
            mid = 0
            while l <= r:
                mid = (l+r)//2
                if g[mid] >= 0:
                    l = mid+1
                else:
                    if g[l] >= 0:
                        r = mid
                    else:
                        index = l
                        break
                                
            count += n - index
            
        return count
