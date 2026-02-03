class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        far = (celsius*1.8)+32.00
        return [celsius+273.15,far]
