class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        cars = [[pos, s] for pos, s in zip(position, speed)]
        cars.sort(reverse=True, key= lambda a: a[0])

        for pos, s in cars:
            time = (target - pos) / s
            
            if not stack:
                stack.append(time)
            
            if stack and stack[-1] < time:
                stack.append(time)
            
        return len(stack)