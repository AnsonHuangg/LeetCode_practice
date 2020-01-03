class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        while s!='':
            if s[0]=='('or s[0]=='{'or s[0]=='[':
                stack.append(s[0])
            elif stack==[]:
                return False
                break
            elif s[0]==')' and stack[-1]=='(':
                stack.pop()
            elif s[0]=='}' and stack[-1]=='{':
                stack.pop()
            elif s[0]==']' and stack[-1]=='[':
                stack.pop()
            else:
                return False
                break
            s = s[1:]
        if stack==[]:
            return True