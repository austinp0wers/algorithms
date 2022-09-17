class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
            