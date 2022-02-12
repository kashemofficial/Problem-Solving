class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s = []
        s += self.postorderTraversal(root.left)
        s += self.postorderTraversal(root.right)
        s += [root.val]
        return s





