import heapq
arr = []
heap = []
heapq.heapify(heap)
for _ in range(int(input())):
    s = input()
    if s[0] == "i":
        n = s.split(" ")
        heapq.heappush(heap,int(n[1]))
    elif s[0] == "r":
        if heap:
            heapq.heappop(heap)
        else:
            arr.append("insert 0")
    else:
        n = s.split(" ")
        if not heap or heap[0] != int(n[1]):
            temp = 0
            while len(heap) > 0:
                temp = heapq.heappop(heap)
                if temp >= int(n[1]):
                    heapq.heappush(heap,temp)
                    break
                arr.append("removeMin")
                
            if len(heap) == 0 or temp!= int(n[1]):
                t = "insert "+n[1]
                heapq.heappush(heap,int(n[1]))
                arr.append(t)
                
    arr.append(s)
    
print(len(arr))
for i in range(len(arr)):
    print(arr[i])