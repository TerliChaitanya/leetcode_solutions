# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        while head:
            if l.pop(-1)!=head.val:
                return False
            head=head.next
        return True

        