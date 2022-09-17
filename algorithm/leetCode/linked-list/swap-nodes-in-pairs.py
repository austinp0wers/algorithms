class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # i've originally wanted to only change the links between the nodes but that didn't work.
        # so this is what i've done. I was NOT satisfied
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        for i in range(1, len(temp),2):
            a = temp.pop(i)
            temp.insert(i-1,a)

        dummy = curr = ListNode()
        for i in range(len(temp)):
            curr.next = ListNode(temp[i])
            curr = curr.next 
        return dummy.next
            

# this is what i've seen someone do. 
# instead of changing the links, you swap the val of the nodes.
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
            
        return cur
