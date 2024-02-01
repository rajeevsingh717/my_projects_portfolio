# 29. Divide Two Integers
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = abs(dividend)
        b = abs(divisor)
        negative = (dividend < 0 and divisor >=0) or (dividend >= 0 and divisor <0)
        output = 0
        while a >= b:
                counter = 1
                decrement = b
                while a >= decrement:
                    # print(counter, counter, decrement, output)
                    a -= decrement
                    output += counter
                    counter += counter
                    decrement += decrement
        output = output if not negative else -output
        return(min(max(output,-2**31),2**31-1))



