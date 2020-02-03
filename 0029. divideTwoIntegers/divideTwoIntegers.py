class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        buf = dividend//divisor
        if buf>2**31-1:
            return 2**31-1
        elif buf<(-1)*2**31:
            return (-1)*2**31
        elif (dividend<0 and divisor<0) or (dividend>0 and divisor>0) or dividend==0:
            return buf
        else:
            if int(abs(dividend/divisor))==abs(dividend/divisor):
                return buf
            else:
                return buf+1