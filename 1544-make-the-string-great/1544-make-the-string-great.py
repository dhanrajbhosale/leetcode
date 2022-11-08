class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for curr in s:
            if not stack:
                stack.append(curr)
                continue
            # add in stack if not small, capital  
            prev = stack.pop()
            if not abs(ord(prev)-ord(curr))==32:
                stack.append(prev)
                stack.append(curr)
        return "".join(stack)
        