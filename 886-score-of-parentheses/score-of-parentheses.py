class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score_stack = [0]
        for char in s:
            if char == "(":
                score_stack.append(0)
            elif score_stack:
                top = score_stack.pop()
                score_stack[-1] += max(1,top*2)
        return score_stack[-1]
