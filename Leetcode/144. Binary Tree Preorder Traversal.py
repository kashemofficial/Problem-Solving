class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s = [root.val]
        s += self.preorderTraversal(root.left)
        s += self.preorderTraversal(root.right)
        return s

