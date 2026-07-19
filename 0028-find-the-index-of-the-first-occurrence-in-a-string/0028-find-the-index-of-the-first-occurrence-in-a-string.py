class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if needle in haystack[i:i+len(needle)]:
                return i
        return -1