class bitCount:
    def count(self,dict,num,s,div,sign1,sign2,sign3,sign4):
        while num%div!=0:
            if num%div==sign1:
                s = dict.get(sign1) + s
                num -= sign1
            elif num%div==sign2:
                s = dict.get(sign2) + s
                num -= sign2
            elif num%div==sign3:
                s = dict.get(sign3) + s
                num -= sign3
            else:
                s = dict.get(sign4) + s
                num -= sign4
        return num,s

class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        dict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        num,s = bitCount().count(dict,num,s,10,4,9,5,1)
        num,s = bitCount().count(dict,num,s,100,40,90,50,10)
        num,s = bitCount().count(dict,num,s,1000,400,900,500,100)
        num,s = bitCount().count(dict,num,s,10000,4000,9000,5000,1000)
        return s