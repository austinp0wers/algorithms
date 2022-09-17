class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = []
        while list1:
            sorted_list.append(list1.val)
            list1 = list1.next
        
        while list2:
            sorted_list.append(list2.val)
            list2 = list2.next
        
        sorted_list.sort()
        
        dummy = curr = ListNode()
        for i in range(len(sorted_list)):
            curr.next = ListNode(sorted_list[i])
            curr = curr.next
        
        return dummy.next