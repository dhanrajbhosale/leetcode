class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                i = stack.pop()
                if (i=='(' and c!=')') or (i=='[' and c!=']') or (i=='{' and c!='}'):
                    return False
        return False if len(stack) else True