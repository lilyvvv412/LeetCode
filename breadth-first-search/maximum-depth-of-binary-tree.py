# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        '''if root is None: return 0
        l_depth=self.maxDepth(root.left)
        r_depth=self.maxDepth(root.right)
        return max(l_depth,r_depth)+1'''
#time O(n), space O(n)
        ans=0
        def f(node,cnt):
            if node is None: return #退出
            cnt+=1
            nonlocal ans #去外层找
            ans=max(ans,cnt)
            f(node.left,cnt)
            f(node.right,cnt)
        f(root,0)
        return ans