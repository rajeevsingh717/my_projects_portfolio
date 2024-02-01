# 12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',
        4:'IV',9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
        sorted_dict = dict(sorted(roman_dict.items(), key=lambda x:x[0], reverse=True))
        r = ''
        for n in sorted_dict:
            while n <= num:
                r += roman_dict[n]
                num -= n
        return r
