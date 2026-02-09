class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        ans = []
        s = str(num)
        n = len(s)
        for i in range(n):
            if n-i == 4:
                ans.append(numerals[1000]*int(s[i]))
                
            else:
                if int(s[i]) < 4:
                    ans.append(numerals[int("1"+("0"*(n-i-1)))]*int(s[i]))
                elif int(s[i]) == 4:
                    ans.append(numerals[int("1"+("0"*(n-i-1)))]+numerals[int("5"+("0"*(n-i-1)))])
                elif int(s[i]) < 9:
                    ans.append(numerals[int("5"+("0"*(n-i-1)))]+(numerals[int("1"+("0"*(n-i-1)))] * (int(s[i])-5)))
                else:
                    ans.append(numerals[int("1"+("0"*(n-i-1)))]+numerals[int("1"+("0"*(n-i)))])

        return "".join(ans)
