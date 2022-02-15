class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, total, operators = [], 0, ['+', '-', '*', '/']

        def operate(op, a, b):
            match op:
                case '+': return a+b
                case '-': return a-b
                case '*': return a*b
                case '/': return int(a/b)

        for e in tokens:
            if e in operators:
                b, a = stack.pop(), stack.pop()
                e = operate(e, a, b)
            stack.append(int(e))

        return stack.pop()


sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*"]))
print(sol.evalRPN(["4", "13", "5", "/", "+"]))
print(sol.evalRPN(["10", "6", "9", "3", "+",
      "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(sol.evalRPN(['4', '3', '-']))
