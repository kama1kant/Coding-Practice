from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while a < 0 and len(stack) > 0 and stack[-1] > 0:
                b = stack.pop()
                if abs(a) < b:
                    stack.append(b)
                    a = 0
                    break
                elif abs(a) == b:
                    a = 0
                    break
            if a != 0:
                stack.append(a)

        return stack


sol = Solution()
print(sol.asteroidCollision([5, 10, -5]))
print(sol.asteroidCollision([8, -8]))
print(sol.asteroidCollision([10, 2, -5]))
print(sol.asteroidCollision([1, -2, -3, 9]))
