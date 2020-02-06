class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while num//10!=0:
            ans = 0
            while num!=0:
                ans += num%10
                num //= 10
            num = ans
            
        return ans
        
print(Solution().addDigits(1))