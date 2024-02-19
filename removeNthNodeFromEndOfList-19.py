# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        leftPointer = head
        rightPointer = head

        while n > 0 and rightPointer:
            rightPointer = rightPointer.next
            n -= 1

        while rightPointer and rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

        if leftPointer == head and not rightPointer:
            return head.next            
        
        leftPointer.next = leftPointer.next.next
        
        return head
    