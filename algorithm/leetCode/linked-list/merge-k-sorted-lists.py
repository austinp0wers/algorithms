class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_array = []
        
        for i in lists:
            while i:
                sorted_array.append(i.val)
                i = i.next
        sorted_array.sort()
        
        answer = current = ListNode() 
        for i in range(len(sorted_array)):
            current.next = ListNode(sorted_array[i])
            current = current.next
        
        return answer.next