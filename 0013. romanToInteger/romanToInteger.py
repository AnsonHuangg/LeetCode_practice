class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        while len(s)!=0:
            if s[0:2]=='CM':
                ans = ans + dict.get('CM')
                s = s[2:]
            elif s[0:2]=='CD':
                ans = ans + dict.get('CD')
                s = s[2:]
            elif s[0:2]=='XC':
                ans = ans + dict.get('XC')
                s = s[2:]
            elif s[0:2]=='XL':
                ans = ans + dict.get('XL')
                s = s[2:]
            elif s[0:2]=='IX':
                ans = ans + dict.get('IX')
                s = s[2:]
            elif s[0:2]=='IV':
                ans = ans + dict.get('IV')
                s = s[2:]
            elif s[0]=='M':
                ans = ans + dict.get('M')
                s = s[1:]
            elif s[0]=='D':
                ans = ans + dict.get('D')
                s = s[1:]
            elif s[0]=='C':
                ans = ans + dict.get('C')
                s = s[1:]
            elif s[0]=='L':
                ans = ans + dict.get('L')
                s = s[1:]
            elif s[0]=='X':
                ans = ans + dict.get('X')
                s = s[1:]
            elif s[0]=='V':
                ans = ans + dict.get('V')
                s = s[1:]
            elif s[0]=='I':
                ans = ans + dict.get('I')
                s = s[1:]
            else:
                break
        return ans


print(Solution().romanToInt('MCMXCIV'))



