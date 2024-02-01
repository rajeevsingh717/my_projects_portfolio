# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if len(stack) > 0 and i == dic[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

        
