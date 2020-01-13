class Solution:
    def intToRoman(self, num: int) -> str:
        ans = num
        s = ''
        dict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        while num%10!=0:
            if num%10==4:
                s = dict.get(4) + s
                num -= 4
            elif num%10==9:
                s = dict.get(9) + s
                num -= 9
            elif num%10==5:
                s = dict.get(5) + s
                num -= 5
            else:
                s = dict.get(1) + s
                num -= 1
                
        while num%100!=0:
            if num%100==40:
                s = dict.get(40) + s
                num -= 40
            elif num%100==90:
                s = dict.get(90) + s
                num -= 90
            elif num%100==50:
                s = dict.get(50) + s
                num -= 50
            else:
                s = dict.get(10) + s
                num -= 10
                
        while num%1000!=0:
            if num%1000==400:
                s = dict.get(400) + s
                num -= 400
            elif num%1000==900:
                s = dict.get(900) + s
                num -= 900
            elif num%1000==500:
                s = dict.get(500) + s
                num -= 500
            else:
                s = dict.get(100) + s
                num -= 100
        
        while num%10000!=0:
            s = dict.get(1000) + s
            num -= 1000
        
        return s