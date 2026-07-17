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
        for i in range(len(l)-1,-1,-1):
            if l[i]!=head.val:
                return False
            head=head.next
        return True

        