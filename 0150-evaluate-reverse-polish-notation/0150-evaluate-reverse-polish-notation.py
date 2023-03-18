class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for symbol in tokens:
            match symbol:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    stack.append(-stack.pop() + stack.pop())
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    stack.append(math.trunc((1 / stack.pop()) * stack.pop()))
                case _:
                    stack.append(int(symbol))
        return stack[0]