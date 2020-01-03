class Solution:
    def isValid(self, s: str) -> bool:
        #sample = ['(', ')', '{', '}', '[',']']
        stack = []
        while s!='':
            if s[0]=='('or s[0]=='{'or s[0]=='[':
                stack.append(s[0])
            elif s[0]==[]:
                return False
                break
            elif s[0]==')' and stack[-1]=='(':
                del stack[-1]
            elif s[0]=='}' and stack[-1]=='{':
                del stack[-1]
            elif s[0]==']' and stack[-1]=='[':
                del stack[-1]
            else:
                return False
                break
            s = s[1:]
        if stack==[]:
            return True
        

Solution().isValid(']')