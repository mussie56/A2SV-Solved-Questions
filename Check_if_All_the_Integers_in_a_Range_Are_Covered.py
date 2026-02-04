class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        merged = []
        temp = ranges[0]
        for i in range(1,len(ranges)):
            if ranges[i][0] <= temp[1]+1:
                temp = [temp[0],max(temp[1],ranges[i][1])]
            else:
                merged.append(temp)
                temp= ranges[i]
        merged.append(temp)

        for i in range(len(merged)):
            if right <= merged[i][1] and left >= merged[i][0]:
                    return True
        return False
