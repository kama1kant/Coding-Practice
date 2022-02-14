class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans, max = [], float(-inf)
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max:
                ans.append(i)
                max = heights[i]
        
        return sorted(ans)
        
        
sol = Solution()
print(sol.findBuildings([4,2,3,1]))
print(sol.findBuildings([4,3,2,1]))
print(sol.findBuildings([1,3,2,4]))