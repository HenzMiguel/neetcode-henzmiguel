class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        for c in s:
            if stack and close.get(stack[-1], False) == c:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0