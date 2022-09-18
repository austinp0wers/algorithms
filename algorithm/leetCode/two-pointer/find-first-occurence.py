class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        str_length = len(needle)
        for i in range(len(haystack) - str_length+1):
            right = i + str_length
            if haystack[i:right] == needle:
                return i
        return -1