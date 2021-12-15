from typing import List
import math


class Solution:
    def originalDigits(self, s: str) -> str:
        counter_char = {}
        counter_digits = {}
        
        for i in range(26):
            counter_char[chr(i + 97)] = 0
        
        for i in range(10):
            counter_digits[i] = 0
              
        for i in range(len(s)):
            if s[i] in counter_char:
                counter_char[s[i]] += 1
            else:
                counter_char[s[i]] = 1
           
        counter_digits[0] = counter_char['z']
        counter_digits[2] = counter_char['w']
        counter_digits[4] = counter_char['u']
        counter_digits[6] = counter_char['x']
        counter_digits[8] = counter_char['g']
        counter_digits[5] = counter_char['f'] - counter_digits[4]
        counter_digits[3] = counter_char['h'] - counter_digits[8]
        counter_digits[7] = counter_char['s'] - counter_digits[6]
        counter_digits[1] = counter_char['o'] - \
        counter_digits[0] - counter_digits[2] - counter_digits[4]
        counter_digits[9] = counter_char['i'] - \
            counter_digits[5] - counter_digits[6] - counter_digits[8]
    
        ans = ""
        for digit in counter_digits:
            for i in range(counter_digits[digit]):
                ans += str(digit)
        
        print(counter_digits)
        return ans
            

sol = Solution()
output = sol.originalDigits("nnei")
print(output)
