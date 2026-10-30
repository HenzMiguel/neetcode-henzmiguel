class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        
        stack = []

        for t in tokens:
            if t in "+-*/":
                a = stack.pop()
                b = stack.pop()

                match t:
                    case "+":
                        stack.append(b + a)
                    case "*":
                        stack.append(b * a)
                    case "-":
                        stack.append(b - a)
                    case "/":
                        stack.append(int(b / a))
            else:
                stack.append(int(t))
        return int(stack[0])
