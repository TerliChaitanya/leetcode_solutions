# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def reverse(node):
            prev=None
            while node:
                nxt=node.next
                node.next=prev
                prev=node
                node=nxt
            return prev
        head=reverse(head)
        i=0
        decimal=0
        temp=head
        while temp:
            if temp.val==1:
                decimal+=2**i
            temp=temp.next
            i+=1
        head=reverse(head)
        return decimal
        