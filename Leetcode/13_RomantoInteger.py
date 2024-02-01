# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        res = 0
        for i in range(0,len(s)):
         
            if i+1 < len(s) and int_dict[s[i+1]] > int_dict[s[i]]:
                res -= int_dict[s[i]]
            else:
                res += int_dict[s[i]]
        return res
