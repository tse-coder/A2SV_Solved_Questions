class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0

        for d in directions:
            if d == 'R':
                stack.append(d)

            elif d == 'S':
                while stack and stack[-1] == 'R':
                    collisions += 1
                    stack.pop()
                stack.append('S')

            else:  # d == 'L'
                if not stack:
                    continue

                if stack[-1] == 'S':
                    collisions += 1
                else:
                    collisions += 2
                    stack.pop()
                    while stack and stack[-1] == 'R':
                        collisions += 1
                        stack.pop()
                stack.append('S')

        return collisions
        
