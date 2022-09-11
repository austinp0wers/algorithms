class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dpCache = [[False for _ in range(len(p) +1)] for _ in range(len(s)+1)]
        dpCache[0][0] = True
        trueUntil = 1
        while trueUntil -1 < len(p):
            if p[trueUntil - 1] != '*':
                break
            dpCache[0][trueUntil] = True
            trueUntil += 1
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '?' or s[i- 1] == p[j-1]:
                    if dpCache[i-1][j-1]:
                        dpCache[i][j] = dpCache[i-1][j-1]
                if p[j - 1] == '*':
                    if dpCache[i-1][j] or dpCache[i][j-1]:
                        dpCache[i][j] = True
        return dpCache[len(s)][len(p)]