class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            flag = True
            while len(stack) and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                flag = False
                break
            if flag:
                stack.append(asteroid)

        return stack