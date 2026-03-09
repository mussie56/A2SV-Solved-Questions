class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.original = k
        self.temp = k

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.temp-=1
            if self.temp == 0:
                self.temp+=1
                return True
        else:
            self.temp = self.original
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)