class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)
        summ = 0
        i = 0
        for i in range(1,len(heights)):
            if heights[i] <= heights[i-1]:
                continue
            diff = heights[i]-heights[i-1]
            if len(heap) < ladders:
                heapq.heappush(heap,diff)
            else:
                if heap and heap[0] < diff:
                    summ+=heapq.heappop(heap)
                    heapq.heappush(heap,diff)
                else:
                    summ+=diff
            if summ > bricks:
                return i-1
                # break

        return i#-1