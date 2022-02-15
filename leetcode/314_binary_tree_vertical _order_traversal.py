from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def verticalOrder(self, root):
        if root is None:
            return root
        ans, que, level = {}, [], 0
        que.append([root, level])

        while len(que) > 0:
            data = que.pop(0)
            node, l = data[0], data[1]

            if l not in ans:
                ans[l] = []
            ans[l].append(node.val)
            if node.left is not None:
                que.append([node.left, l-1])
            if node.right is not None:
                que.append([node.right, l+1])

        ans = sorted(list(ans.items()), key=lambda x: x[0])
        ans = [v[1] for v in ans]
        return ans


# drawtree(deserialize('[3,9,8,4,0,1,7,null,null,null,2,5]'))
sol = Solution()
print(sol.verticalOrder('[3,9,8,4,0,1,7]'))
print(sol.verticalOrder('[3,9,8,4,0,1,7,null,null,null,2,5]'))
