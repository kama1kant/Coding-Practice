class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        sum = 0
        
        def backtrack(arr, depth):
            nonlocal sum
            for e in arr:
                if e.isInteger():
                    sum += e.getInteger() * depth
                else:
                    backtrack(e.getList(), depth+1)

        backtrack(nestedList, 1)
        return sum