class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for value in tokens:
            if value =="+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif value =="-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif value =="*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif value =="/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(value))
        return stack[-1]   


        