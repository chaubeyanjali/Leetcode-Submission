class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open, close):
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

            if open == n and close == n:
                result.append("".join(stack))

        backtrack(0, 0)

        return result
        
        