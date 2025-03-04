class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []

        for char in arr:
            if char == "..":
                if stack:
                    stack.pop()

            elif char == "." or not char:
                continue
            else:
                stack.append(char)

        return "/" + "/".join(stack)
            