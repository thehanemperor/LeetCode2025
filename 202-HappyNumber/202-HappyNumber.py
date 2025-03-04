class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n !=1:
            curr = self.calc(n)
            if curr in seen:
                return False
            seen.add(curr)
            n = curr

        return True

    def calc(self,n):
        total = 0
        
        while n !=0:
            mod = n%10
            n //= 10
            total += mod**2

        return total