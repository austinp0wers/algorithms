class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(arr = [], left = 0, right = 0):
            if len(arr) == 2 * n:
                answer.append("".join(arr))
                return
            if left < n:
                arr.append('(')
                backtrack(arr, left+1, right)
                arr.pop()
            if right < left:
                arr.append(')')
                backtrack(arr,left, right+1)
                arr.pop()
        backtrack()
        return answer

# when solving backtracking questions, always remember to pop the last element
# or else, the length of the arr will just stay the same.
