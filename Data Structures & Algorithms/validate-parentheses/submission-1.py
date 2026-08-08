class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "{[(":
                stack.append(c)
            elif c in "}])":
                if not stack:
                    return False
                matching_bracket = stack.pop()
                if c == "}" and matching_bracket != "{":
                    return False
                if c == "]" and matching_bracket != "[":
                    return False
                if c == ")" and matching_bracket != "(":
                    return False
        return not stack
            