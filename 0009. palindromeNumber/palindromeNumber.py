class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0
        if x<0:
            return "False"
        else:
            y = x
            while y/10 >= 1:
                buf = y % 10
                ans = ans*10+buf
                y //= 10
            buf = y % 10
            ans = ans*10+buf
            if x==ans:
                return "True"
            else:
                return "False"
