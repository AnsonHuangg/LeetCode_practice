class bitCount:
    def count(self,dict,num,s):
        if num%100==10:
            s = dict.get(10) + s
        elif num%100==11:
            s = dict.get(11) + s
        elif num%100==12:
            s = dict.get(12) + s
        elif num%100==13:
            s = dict.get(13) + s
        elif num%100==14:
            s = dict.get(14) + s
        elif num%100==15:
            s = dict.get(15) + s
        elif num%100==16:
            s = dict.get(16) + s
        elif num%100==17:
            s = dict.get(17) + s
        elif num%100==18:
            s = dict.get(18) + s
        elif num%100==19:
            s = dict.get(19) + s
        else:
            if num%10==1:
                s = dict.get(1) + s
            elif num%10==2:
                s = dict.get(2) + s
            elif num%10==3:
                s = dict.get(3) + s
            elif num%10==4:
                s = dict.get(4) + s
            elif num%10==5:
                s = dict.get(5) + s
            elif num%10==6:
                s = dict.get(6) + s
            elif num%10==7:
                s = dict.get(7) + s
            elif num%10==8:
                s = dict.get(8) + s
            elif num%10==9:
                s = dict.get(9) + s
            num2 = num // 10
            if num2%10==2:
                s = dict.get(20) + s
            elif num2%10==3:
                s = dict.get(30) + s
            elif num2%10==4:
                s = dict.get(40) + s
            elif num2%10==5:
                s = dict.get(50) + s
            elif num2%10==6:
                s = dict.get(60) + s
            elif num2%10==7:
                s = dict.get(70) + s
            elif num2%10==8:
                s = dict.get(80) + s
            elif num2%10==9:
                s = dict.get(90) + s
            else:
                s = s
        
        num //= 100
        
        if num%10==1:
            s = dict.get(1) + dict.get(100) + s
        elif num%10==2:
            s = dict.get(2) + dict.get(100) + s
        elif num%10==3:
            s = dict.get(3) + dict.get(100) + s
        elif num%10==4:
            s = dict.get(4) + dict.get(100) + s
        elif num%10==5:
            s = dict.get(5) + dict.get(100) + s
        elif num%10==6:
            s = dict.get(6) + dict.get(100) + s
        elif num%10==7:
            s = dict.get(7) + dict.get(100) + s
        elif num%10==8:
            s = dict.get(8) + dict.get(100) + s
        elif num%10==9:
            s = dict.get(9) + dict.get(100) + s
        else:
            s = s

        return s

class Solution:
    def numberToWords(self, num: int) -> str:
        dict = {1:' One',2:' Two',3:' Three',4:' Four',5:' Five',6:' Six',7:' Seven',8:' Eight',9:' Nine',
        10:' Ten',11:' Eleven',12:' Twelve',13:' Thirteen',14:' Fourteen',15:' Fifteen',16:' Sixteen',17:' Seventeen',18:' Eighteen',19:' Nineteen',
        20:' Twenty',30:' Thirty',40:' Forty',50:' Fifty',60:' Sixty',70:' Seventy',80:' Eighty',90:' Ninety',
        100:' Hundred',1000:' Thousand',1000000:' Million',1000000000:' Billion'}
        s=''
        count = 0
        
        while num!=0:
            if count==1 and num%1000!=0:
                s = dict.get(1000) + s
            elif count==2 and num%1000!=0:
                s = dict.get(1000000) + s
            elif count==3 and num%1000!=0:
                s = dict.get(1000000000) + s
            
            count += 1
            
            num_div = num%1000
            num //= 1000
            s = bitCount().count(dict,num_div,s)
        
        if s=='':
            s = 'Zero'
        elif s[0]==' ':
            s = s[1:]
        return s