class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        else:
            return (num-1)%9 + 1