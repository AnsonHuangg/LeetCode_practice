class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = str(x)
        ans_buf = ans[::-1]
        if ans==ans_buf:
            return True
        else:
            return False