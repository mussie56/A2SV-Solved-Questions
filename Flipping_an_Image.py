class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range(n//2):
                image[i][j],image[i][n-1-j] = image[i][n-1-j],image[i][j]

        for i in range(n):
            for j in range(n):
                image[i][j] = (image[i][j]+1)%2

        return image
