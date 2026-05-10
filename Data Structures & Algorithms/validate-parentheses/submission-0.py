class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {')': '(', '}' : '{', ']' : '['}
        for c in s:
            if c in characters.values():
                stack.append(c)
            else:
                if len(stack) <= 0 or stack[-1] != characters[c]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0

        