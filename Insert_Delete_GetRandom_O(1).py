class RandomizedSet:

    def __init__(self):
        self.rand = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.rand:
            self.arr.append(val)
            self.rand[val] = len(self.arr)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.rand:
            temp = self.rand[val]
            self.arr[-1],self.arr[temp] = self.arr[temp], self.arr[-1]
            self.rand[self.arr[temp]] = temp
            self.arr.pop()
            del self.rand[val]
            return True
        return False

    def getRandom(self) -> int:
        rand_index = random.randint(0,len(self.arr)-1)
        return self.arr[rand_index]
