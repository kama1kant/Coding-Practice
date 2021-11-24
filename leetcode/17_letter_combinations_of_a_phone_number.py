from typing import List


class Solution:
   def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        
        def getLetters(digits, index, char_bag):
            nonlocal ans
            if(index >= len(digits)):
                ans.append("".join(char_bag))
                return
            for character in keypad[digits[index]]:
                char_bag.append(character)
                getLetters(digits, index+1, char_bag)
                char_bag.pop()  # Don't use char_bag.remove(character)
            return
                
        keypad = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], 
                    '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], 
                    '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
                    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        if len(digits) > 0:
            getLetters(digits, 0, [])
        return ans
        
sol = Solution()
output = sol.letterCombinations("23")
print(output)