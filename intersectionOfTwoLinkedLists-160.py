# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        firstPointer = headA
        secondPointer = headB

        while firstPointer != secondPointer:
            firstPointer = firstPointer.next if firstPointer != None else headB
            secondPointer = secondPointer.next if secondPointer != None else headA

        return firstPointer