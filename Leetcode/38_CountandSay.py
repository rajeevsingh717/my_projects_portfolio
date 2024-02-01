"""The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: 
            return "1"
        elif n==2: 
            return "11"
        else:
            val = "11"
            i = 2
            while i < n:
                count , final = 1, ""
                print(val)
                for j in range(0,len(val)):
                    if j+1 < len(val) and val[j] == val[j+1]:
                        count += 1
                    else:
                        final +=  str(count) + val[j]
                        count = 1
                val = final 
                i += 1
        return val



        
