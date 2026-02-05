class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        char = {}
        for c in chars:
            char[c] = char.get(c,0)+1
        
        for word in words:
            wo = {}
            nope = False
            for w in word:
                wo[w] = wo.get(w,0)+1
            for key in wo:
                if wo[key] > char.get(key,0):
                    nope = True
                    break
            if not nope:
                count+=len(word)
        return count
