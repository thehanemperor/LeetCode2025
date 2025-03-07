class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                second = stack.pop()
                first = stack.pop()
                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(first - second)
                elif t == "*":
                    stack.append(first * second)
                elif t == "/":
                    if first * second < 0:
                        curr = abs(first) // abs(second)
                        stack.append(-curr)
                    else:
                        stack.append(first // second)

            else:
                stack.append(int(t))
        
        return stack[0]