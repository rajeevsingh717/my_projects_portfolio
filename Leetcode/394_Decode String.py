"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        final = ''
        curr = ''
        for i in range(0,len(s)):
            if s[i] != ']':
                stack.append(s[i]) ## append in the stack until we find the closing bracket ']'
            else:
                charset = ''
                while stack[-1] != '[':
                    charset += stack.pop()
                stack.pop() ## removing the '[' char
                n=''
                while len(stack) != 0 and stack[-1].isdigit() == True:
                    n += stack.pop() ## collecting all the numeric digit
                
                charsofar = charset*int(n[::-1]) ## calcualting the list of char so far with given pattern and occurance
                stack.append(charsofar) ## apending it back to the top of stack
        print(stack)

        final = ''.join([word[::-1] for word in stack]) ## concatenating all the words in the stack
        return final
            

           
        
       
