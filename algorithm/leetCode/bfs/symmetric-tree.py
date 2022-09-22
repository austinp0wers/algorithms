class Solution:
    def isMirror(self, left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        if left.val == right.val:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right,right.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)    