class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in pairs.keys():
                stack.append(c)
            else:
                if len(stack) > 0 and c == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0