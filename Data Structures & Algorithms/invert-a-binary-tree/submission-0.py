# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        if root.right and root.left:
            root.right = self.invertTree(root.right)
            root.left = self.invertTree(root.left)
            self.branchSwitch(root)

        elif root.right:
            root.right = self.invertTree(root.right)
            self.branchSwitch(root)

        elif root.left:
            root.left = self.invertTree(root.left)
            self.branchSwitch(root)
        
        return root
    
    def branchSwitch(self, root: Optional[TreeNode]) -> None:
        new_right = root.left
        new_left = root.right
        root.right = new_right
        root.left = new_left

