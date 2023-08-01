def hasCycle(self, head: Optional[ListNode]) -> bool:
        #using slow and fast pointers
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
