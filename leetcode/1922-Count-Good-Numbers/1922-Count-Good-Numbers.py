class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        even = (n + 1) // 2
        odd = n // 2
        def helper(base: int, exp: int,mod: int) -> int:
            res = 1
            while exp > 0:
                if exp%2:
                    res = (res*base)%mod
                base = (base*base)%mod
                exp//=2
            return res

        return (helper(5,even,mod)*helper(4,odd,mod))%mod