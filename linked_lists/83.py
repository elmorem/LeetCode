# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        cur = head
        while cur:
            while cur.next is not None and cur.val == cur.next.val :
                cur.next = cur.next.next
            cur = cur.next
        return head