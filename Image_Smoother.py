class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(img)
        m = len(img[0])
        for i in range(n):
            temp = []
            for j in range(m):
                count = 0
                summ = 0
                for k in range(max(0,i-1),min(n,i+2)):
                    for l in range(max(0,j-1),min(m,j+2)):
                        count+=1
                        summ+=img[k][l]

                temp.append(summ//count)

            ans.append(temp)

        return ans
