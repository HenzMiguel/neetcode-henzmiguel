class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        temp = []

        while len(self.q) > 1:
            temp.append(self.q.pop(0))
        
        res = self.q.pop(0)
        self.q = temp

        return res

    def top(self) -> int:
        temp = []

        while len(self.q) > 1:
            temp.append(self.q.pop(0))
        
        res = self.q.pop(0)
        temp.append(res)
        self.q = temp

        return res

    def empty(self) -> bool:
        return len(self.q) <= 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()