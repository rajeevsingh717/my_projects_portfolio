"""You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = []
        calc = 0
        for i in range(0,len(tokens)):
            if tokens[i] not in ['+','-','*','/']:
                stack.append(int(tokens[i]))
            else:
                if len(stack) == 1:
                    return stack[0]
                val2 = stack.pop()
                val1 = stack.pop()
                if tokens[i] == '+':
                    calc = val1 + val2
                elif tokens[i] == '-':
                    calc = val1 - val2
                elif tokens[i] == '*':
                    calc = val1 * val2
                else:
                    calc = int(val1 / val2)
                stack.append(calc)
        return stack[0]
                

