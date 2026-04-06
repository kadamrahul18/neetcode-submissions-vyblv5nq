class Solution:
    def is_operand(self, c):
        if c == "+" or c == "-" or c == '*' or c == '/':
            return True
        else:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in '+-*/':
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if c == "+":
                    stack.append(op1 + op2)
                if c == "-":
                    stack.append(op2 - op1)
                if c == '*':
                    stack.append(op2 * op1)
                if c == '/':
                    stack.append(int(op2 / op1))
            else:
                stack.append(c)
        return int(stack[-1])

            