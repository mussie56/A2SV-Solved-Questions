class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for i in matrix:
            for j in range(min(k,len(i))):
                heapq.heappush(heap,-i[j])
                if len(heap) > k:
                    heapq.heappop(heap)

        return heap[0] * (-1)