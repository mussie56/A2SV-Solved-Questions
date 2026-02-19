class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        summ = 0
        for i in range(1,n-n//3,2):
            summ+=piles[i]

        return summ
