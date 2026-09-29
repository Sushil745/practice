# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Create a dummy node to act as the head of the resulting list
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Loop until both lists are fully traversed and there is no remaining carry
        while l1 or l2 or carry:
            # Get the values from the current nodes, defaulting to 0 if the list ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            out_val = total % 10
            
            # Create a new node with the single-digit result and advance the tracker
            curr.next = ListNode(out_val)
            curr = curr.next
            
            # Move to the next nodes in the input lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next
