class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move = 0
        while maxDoubles > 0 and target > 1:
            move+=target%2+1
            target //= 2
            maxDoubles-=1
        return move+target-1