class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root, float("-inf"), float("inf"))
        
    def validateBST(self, node, left, right):
        if not node:
            return True
        if not (left < node.val and right > node.val):
                return False
        else:
            return self.validateBST(node.left, left, node.val) and self.validateBST(node.right, node.val, right)