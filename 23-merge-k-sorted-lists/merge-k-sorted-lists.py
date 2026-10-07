# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to easily build the merged linked list
        dummy = ListNode(0)
        curr = dummy
        
        # Initialize the min-heap
        heap = []
        
        # Push the head of each linked list into the heap
        # We include the index 'i' to avoid comparing ListNode objects directly if values are equal
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
                
        # Process the heap until it's empty
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Append the smallest node to the result list
            curr.next = node
            curr = curr.next
            
            # If there is a next node in the same list, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next