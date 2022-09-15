class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return
        table = {'2': ['a','b','c'],'3': ['d','e','f'], 
                '4': ['g','h','i'], '5': ['j','k','l'], 
                '6': ['m','n','o'], '7': ['p','q','r','s'], 
                '8': ['t','u','v'], '9': ['w','x','y','z']}
        answer = []
        def backtracking(index, arr ):
            if len(arr) == len(digits):
                answer.append("".join(arr))
                return 
            else:
                for i in range(len(table[digits[index]])):
                    arr.append(table[digits[index]][i])
                    backtracking(index+1, arr)
                    arr.pop()
                    
        backtracking(0,[])
        return answer