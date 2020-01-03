class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        count = 0
        while len(haystack)>=len(needle):
            if haystack[0:len(needle)]==needle:
                return count
                break
            else:
                haystack = haystack[1:]
                count += 1
                    
        if len(haystack)<len(needle):
            return -1