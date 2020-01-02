class Solution:
    def reverse(self, x: int) -> int:
        if x>(2**31)-1 or x<(2**31)*(-1) or x==0:
            return 0
        else:
            ans = str(x)
            while ans[-1]=='0':
                ans = ans[:-1]
            if ans[0]=='-':
                ans = ans[1:]
            a = int(ans[::-1])
            if a>(2**31)-1 or a<(2**31)*(-1):
                return 0
            elif x>0:
                return a
            else:
                return a*(-1)