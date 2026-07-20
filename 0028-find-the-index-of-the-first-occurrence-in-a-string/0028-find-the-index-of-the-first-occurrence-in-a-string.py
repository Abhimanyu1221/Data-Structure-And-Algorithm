class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x=len(haystack)
        y=len(needle)
        
        for i in range(x-y+1):
            for j in range(y):
                if needle[j] != haystack[i+j]:
                    break
                if j == y-1:
                    return i
        return -1