from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit, alpha = [], []
        for log in logs:
            [id, data] = log.split(' ', 1)
            data = data.strip()
            if data[0].isnumeric(): 
                digit.append([id, data])
            else: 
                alpha.append([id, data])
        
        alpha = sorted(alpha, key=lambda x:(x[1], x[0]))
        digit, alpha = [' '.join(d) for d in digit], [' '.join(a) for a in alpha]
        return alpha + digit
        
        
        
        
sol = Solution()
print(sol.reorderLogFiles(["dig1  8 1 5 1","let3 art can","dig2 3 6","let2 own kit dig","let1 art zero"]))
print(sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))