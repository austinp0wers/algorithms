# just a simple recursion
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# bfs using queue
# but for some reason this takes longer and takes up little more memory
class Solution:
    def def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = deque([(p,q)])
        max_q_size = 0
        while que:
            max_q_size = max(max_q_size, len(que))
            p, q = que.popleft()
            if not p and not q:
                continue
            elif (not p or not q) or (p.val != q.val):
                return False
            que.extend([(p.left, q.left), (p.right, q.right)])
        return True