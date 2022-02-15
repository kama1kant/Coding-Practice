class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dict, b, c = {str(e): 0 for e in range(10)}, 0, 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
            else:
                if dict[secret[i]] < 0:
                    c += 1
                if dict[guess[i]] > 0:
                    c += 1

                dict[secret[i]] += 1
                dict[guess[i]] -= 1

        return str(b)+'A'+str(c)+'B'


sol = Solution()
print(sol.getHint('1807', '7810'))
print(sol.getHint('1123', '0111'))
