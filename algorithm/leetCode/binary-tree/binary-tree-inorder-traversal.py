class Solution:
    def traverse(self, node, answer):
        if node.left:
            self.traverse(node.left, answer)
        
        answer.append(node.val)
        
        if node.right:
            self.traverse(node.right, answer)
            
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root:
            self.traverse(root, answer)
        
        return answer 