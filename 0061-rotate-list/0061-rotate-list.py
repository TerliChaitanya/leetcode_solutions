# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0 or not head.next:
            return head
        l=1
        temp=head
        while temp.next:
            l+=1
            temp=temp.next
        k=k%l
        if k==0:
            return head
        temp=head
        for _ in range(l-k-1):
            temp=temp.next
        new_head=temp.next
        temp.next=None
        temp=new_head
        while temp.next:
            temp=temp.next
        temp.next=head
        return new_head
