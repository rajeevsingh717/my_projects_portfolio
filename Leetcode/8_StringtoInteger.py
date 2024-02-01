# 8. String to Integer (atoi)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.replace(' ','')
        if not s: return 0
        flg = -1 if s[0]=='-' else 1
        i = 1 if s[0] in ['-','+'] else 0
        res = 0
        while i < len(s):
            print(res)
            if  s[i].isalpha() or s[i] in ['.','+','-']:
                break
            else:
                new = int(s[i])
                res = (res*10) + new
            i += 1
        
        if res*flg >= 2**31:
            return 2**31-1
        elif res*flg <= -2**31:
            return -2**31
        else: 
            return res*flg

      
