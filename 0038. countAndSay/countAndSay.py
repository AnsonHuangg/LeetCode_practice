class Solution:
    def countAndSay(self, n: int) -> str:
        a = 1
        ans = 1
        count = 1
        while a<n:
            ans_buf = 0
            sig_diff = 0
            while ans%10!=0:
                buf1 = ans % 10
                ans = ans // 10
                buf2 = ans % 10
                if buf2==buf1:
                    count += 1
                else:
                    ans_buf = ans_buf + (100**sig_diff)*(buf1+10*count)
                    count = 1
                    sig_diff += 1
                    if buf2==0:
                        break
            ans = ans_buf
            a += 1
        answer = str(ans)
        return answer