class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #new_approach
        #first and slow  node declare
        fast = head
        slow = head
        for i in range(n):#iterating towards fast's next node declare
            fast = fast.next

        if not fast: return head.next#printing head's next if its slow node
        while fast.next:#iterating to both fast and slow next node 
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next#slow node's next dynamic allocation
        return head#printing head after the ll's nth node removal


        #old_approach
        #h1=head;h2=head
        #for i in range(n):
         #   h1=h1.next
          #  if not h1:return head.next
           # while h1.next:
            #    h2=h2.next;h1=h1.next
             #   h2.next=h2.next.next
       # return head
