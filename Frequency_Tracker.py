class FrequencyTracker:

    def __init__(self):
        self.frequency = {}
        self.frequencies = defaultdict(int)

    def add(self, number: int) -> None:
        self.frequency[number] = self.frequency.get(number,0)+1
        after = self.frequency[number]
        self.frequencies[after]+=1
        if after > 1:
            self.frequencies[after-1]-=1
            if self.frequencies[after-1] == 0:
                del self.frequencies[after-1]

    def deleteOne(self, number: int) -> None:
        if number in self.frequency:
            before = self.frequency[number]
            self.frequency[number] -= 1 
            if self.frequency[number] == 0:
                del self.frequency[number]

            self.frequencies[before]-=1
            if self.frequencies[before] == 0:
                del self.frequencies[before]
            if before > 1:
                self.frequencies[before-1]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.frequencies
