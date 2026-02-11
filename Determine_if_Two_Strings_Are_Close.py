class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = set(word1)
        w2 = set(word2)
        if w1 == w2:
            arr1 = [0]*26
            arr2 = [0]*26

            for i in word1:
                ch = ord(i)-97
                arr1[ch] += 1

            for i in word2:
                ch = ord(i)-97
                arr2[ch] += 1
            
            freq1 = Counter(arr1)
            freq2 = Counter(arr2)

            return freq2 == freq1

        return False
