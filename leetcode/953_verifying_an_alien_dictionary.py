class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        translated_words = []
        for w in words:
            new_w = ''
            for i,c in enumerate(w):
                new_w += chr(order.index(c) + ord('a'))
            translated_words.append(new_w)
        return sorted(translated_words) == translated_words
        
sol = Solution()
print(sol.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))