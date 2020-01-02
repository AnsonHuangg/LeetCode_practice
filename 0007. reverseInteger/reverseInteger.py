class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        y = abs(x)

        while y/10 >= 1:
            buf = y % 10
            ans = ans*10+buf
            y //= 10
        buf = y % 10
        ans = ans*10+buf
        
        if ans>(2**31)-1 or ans<(2**31)*(-1):
            return 0
        elif x>0:
            return ans
        else:
            return ans*(-1)