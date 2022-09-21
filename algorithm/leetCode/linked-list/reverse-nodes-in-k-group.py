# definitely one of the hardest questions.
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nodeBeforeGroup = dummy
        while True:
            kthNode = self.findK(nodeBeforeGroup, k)
            if not kthNode:
                break
            
            nodeAfterGroup = kthNode.next
            cur = nodeBeforeGroup.next
            prev = kthNode.next
            while cur != nodeAfterGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            #it was hard because of this part.
            #I'm essentially linking the last node of previous group to the 
            # changed First node (kthNode) of the next group
            # temp should be the nodeBeforeGroup since it is reversed
            temp = nodeBeforeGroup.next
            nodeBeforeGroup.next = kthNode
            nodeBeforeGroup = temp
            
        return dummy.next
            
    def findK(self, curr, k):
        while curr and k > 0:
                k-= 1
                curr = curr.next
        return curr
            
        return dummy.next