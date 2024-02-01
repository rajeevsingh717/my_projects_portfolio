# 7. Reverse Integer
class Solution:
    
    def reverse(self, x: int) -> int:
        max_int = 2**31 - 1
        sx = str(x)
        sign = -1 if sx[0] == "-" else 1
        final_number = sx if sx[0] != "-" else sx[1:]
        rev_number = final_number[::-1]

        return sign*int(rev_number) if int(rev_number) <= max_int else 0






