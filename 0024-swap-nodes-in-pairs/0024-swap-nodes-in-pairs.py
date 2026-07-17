# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0,head)
        prev=dum
        while prev.next and prev.next.next:
            first=prev.next
            sec=first.next
            first.next=sec.next
            prev.next=sec
            sec.next=first
            prev=first
        return dum.next
