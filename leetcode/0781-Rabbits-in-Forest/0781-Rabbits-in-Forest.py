class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = Counter(answers)
        summ = 0
        for i in answers:
            if i in rabbits:
                summ+=i+1
                rabbits[i] -= min(rabbits[i], i+1)
                if rabbits[i] <= 0:
                    del rabbits[i]
        return summ