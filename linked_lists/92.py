# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        leftPrev = dummy
        cur = head
        for i in range(left-1):
            leftPrev = cur
            cur = cur.next
        prev = None
        for i in range ((right-left) + 1):
                tmpNext = cur.next
                cur.next = prev
                prev = cur
                cur = tmpNext

        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next


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

    # Test case 1: [1,2,3,4,5], left=2, right=4 -> [1,4,3,2,5]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseBetween(head1, 2, 4)
    print(f"Test 1: {linked_list_to_list(result1)}")  # Expected: [1, 4, 3, 2, 5]

    # Test case 2: [5], left=1, right=1 -> [5]
    head2 = create_linked_list([5])
    result2 = solution.reverseBetween(head2, 1, 1)
    print(f"Test 2: {linked_list_to_list(result2)}")  # Expected: [5]

    # Test case 3: [1,2,3], left=1, right=3 -> [3,2,1]
    head3 = create_linked_list([1, 2, 3])
    result3 = solution.reverseBetween(head3, 1, 3)
    print(f"Test 3: {linked_list_to_list(result3)}")  # Expected: [3, 2, 1]

    # Test case 4: [1,2,3,4,5], left=1, right=5 -> [5,4,3,2,1]
    head4 = create_linked_list([1, 2, 3, 4, 5])
    result4 = solution.reverseBetween(head4, 1, 5)
    print(f"Test 4: {linked_list_to_list(result4)}")  # Expected: [5, 4, 3, 2, 1]