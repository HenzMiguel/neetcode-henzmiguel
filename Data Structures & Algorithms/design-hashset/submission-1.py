class MyHashSet:

    def __init__(self):
        self.keys = [[] for i in range(20)]

    def add(self, key: int) -> None:
        slot = key % 10
        if key not in self.keys[slot]:
            self.keys[slot].append(key)

    def remove(self, key: int) -> None:
        slot = key % 10
        if key in self.keys[slot]:
            self.keys[slot].remove(key)

    def contains(self, key: int) -> bool:
        slot = key % 10
        if key in self.keys[slot]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)