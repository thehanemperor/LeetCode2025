class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = 10*num + int(char)

            elif char == "+":
                res += sign * num
                num = 0
                sign = 1
            elif char == "-":
                res += sign * num
                num = 0
                sign = -1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif char == ")":
                res += sign*num
                num = 0
                res *= stack.pop()
                res += stack.pop()

        if num!=0:
            res += sign* num
        return res