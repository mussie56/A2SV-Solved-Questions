class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        while True:
            length = len(res)//2 
            index = 0
            for i in range(1,n-length):
                if arr[index] < arr[i]:
                    index = i
            if index > 1 or n-length > 2:        
                l,r = 0,index
                while l < r:
                    arr[l],arr[r] = arr[r],arr[l]
                    l+=1
                    r-=1

                l,r = 0,n-length-1
                while l < r:
                    arr[l],arr[r] = arr[r],arr[l] 
                    l+=1
                    r-=1
                     
                res.append(index+1)
                res.append(n-length)
            else:
                if index == 0 and len(arr) > 1:
                    res.append(2)
                    arr[0],arr[1] = arr[1],arr[0]
                break
        return res
