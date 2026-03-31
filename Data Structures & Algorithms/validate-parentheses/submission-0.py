class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for letter in s:
            if len(stack) == 0 or dic.get(letter, None) != stack[-1]:
                stack.append(letter)
            else:
                stack.pop()
        return True if len(stack) == 0 else False