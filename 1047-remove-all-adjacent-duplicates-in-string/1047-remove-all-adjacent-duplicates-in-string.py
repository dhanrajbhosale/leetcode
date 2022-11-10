class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for curr in s:
            if not stack:
                stack.append(curr)
                continue
            prev = stack.pop()
            # if duplicate char, skip those
            if prev==curr:
                continue
            stack.append(prev)
            stack.append(curr)
        return "".join(stack)
        