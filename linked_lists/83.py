# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        cur = head
        while cur:
            while cur.next is not None and cur.val == cur.next.val :
                cur.next = cur.next.next
            cur = cur.next
        return head


# Helper functions for testing
def create_linked_list(values: list) -> Optional[ListNode]:
    """Create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Convert a linked list to a Python list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: [1,1,2] -> [1,2]
    head1 = create_linked_list([1, 1, 2])
    result1 = solution.deleteDuplicates(head1)
    print(f"Test 1: {linked_list_to_list(result1)}")  # Expected: [1, 2]

    # Test case 2: [1,1,2,3,3] -> [1,2,3]
    head2 = create_linked_list([1, 1, 2, 3, 3])
    result2 = solution.deleteDuplicates(head2)
    print(f"Test 2: {linked_list_to_list(result2)}")  # Expected: [1, 2, 3]

    # Test case 3: Empty list
    head3 = create_linked_list([])
    result3 = solution.deleteDuplicates(head3)
    print(f"Test 3: {linked_list_to_list(result3)}")  # Expected: []

    # Test case 4: Single element
    head4 = create_linked_list([1])
    result4 = solution.deleteDuplicates(head4)
    print(f"Test 4: {linked_list_to_list(result4)}")  # Expected: [1]