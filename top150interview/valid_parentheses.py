class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        begin = "({["
        end = ")}]"

        for elt in s:
            if elt in begin:
                stack.append(elt)
            elif elt in end:
                if len(stack) == 0:
                    return False
                elif end.index(elt) != begin.index(stack.pop()):
                    return False

        return len(stack) == 0
