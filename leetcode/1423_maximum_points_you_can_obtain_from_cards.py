from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxSum, n = sum(cardPoints[:k]), len(cardPoints)
        if n == k:
            return maxSum

        curSum = maxSum
        for i in range(k):
            curSum = curSum - cardPoints[k-1-i] + cardPoints[n-1-i]
            maxSum = max(maxSum, curSum)

        return maxSum


sol = Solution()
print(sol.maxScore([1,2,3,4,5,6,1], 3))
print(sol.maxScore([2,2,2], 2))
print(sol.maxScore([9,7,7,9,7,7,9], 7))
print(sol.maxScore([1,79,80,1,1,1,200,1], 3))