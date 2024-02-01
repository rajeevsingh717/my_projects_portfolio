""" Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t. """

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        countT, window = {}, {} ## creating 2 dictionary , one for target and 2nd for given string
        
        countT = {i:0 for i in t} ## initializing the target string dictionary with 1
        window = {i:0 for i in s} ## initializing the given string dictionary with 1

        for c in t:
            countT[c] += 1 ## adding the occurance, if certain char has more than 1 occurance 
        
        have, need = 0, len(countT) ## variable to compare if the given string and target string dictionary is complete
        res, reslen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c= s[r]
            window[c] += 1 
            if c in countT and window[c] == countT[c]: ## if the current char in the target dictionary and there occurance also matches
                have += 1 
            
            while have==need: ## once both dictionary satisfy the criteria , time to shrink the window
               
                if (r-l+1) < reslen:  #update the result
                    res = [l , r] ## update the res variable with left and right index
                    reslen = (r -l + 1) ## update the reslen variable as long as have and need are equal
                
                window[s[l]] -= 1 #pop from the left of the window, shrinking the window
                if s[l] in countT and window[s[l]] < countT[s[l]]: ## if the removed left char present in target dcitionary and give string dictionary occurance is less than the target char occurance then update the "have" variable
                    have -= 1
                l += 1 ## keep incrasing the left pointer until it breaks the criteria
        
        
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else "" ## return the result if even single window found else return blank
        
             
            
