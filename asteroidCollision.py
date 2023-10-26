class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ast_len = len(asteroids)
        for i in range(ast_len):
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                collision = asteroids[i] + stack[-1]
                if collision < 0:
                    stack.pop()
                elif collision > 0:
                    asteroids[i] = 0
                else:
                    asteroids[i] = 0
                    stack.pop()

            if asteroids[i]:
                stack.append(asteroids[i])

        return stack


"""
Time - O(N)
Space - O(N)
"""

