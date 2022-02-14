from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans, search, products = [], '', sorted(products)
        for c in searchWord:
            search += c
            i = bisect.bisect_left(products, search)
            j, suggestions = i, []
            
            while j < i+3 and j < len(products):
                if search in products[j]:
                    suggestions.append(products[j])
                else:
                    break
                j += 1

            ans.append(suggestions) if len(suggestions) > 0 else ans.append([])
        
        return ans
        
sol = Solution()
print(sol.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mok"))
print(sol.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags"))