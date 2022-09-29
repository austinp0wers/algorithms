from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque([root])
        answer =[]
        while que:
            temp = []
            for i in range(len(que)):
                cur = que.popleft()
                if cur:
                    que.append(cur.left)
                    que.append(cur.right)
                    temp.append(cur.val)
            if temp:
                answer.append(temp)
        return answer