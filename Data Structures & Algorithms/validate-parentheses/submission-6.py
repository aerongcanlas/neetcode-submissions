class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
                continue

            if not stack or c != self.getMatch(stack.pop()):
                return False


        return not stack
            

    def getMatch(self, bracket: str) -> str:
        if bracket == '(':
            return ')'
        if bracket == '{':
            return '}'
        if bracket == '[':
            return ']'