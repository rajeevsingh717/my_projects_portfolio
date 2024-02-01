# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits :
            return []
        num_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def backtrack(combination,next_digit):
            if len(next_digit)==0:
                output.append(combination)
            else:
                for letter in num_dict[next_digit[0]]:
                    print(combination+letter)
                    backtrack(combination+letter,next_digit[1:])
        
        output = []
        backtrack("",digits)
        return output



                



