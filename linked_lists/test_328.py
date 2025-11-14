import pytest
from typing import Optional
import sys
from pathlib import Path

# Add parent directory to path to import the solution
sys.path.insert(0, str(Path(__file__).parent))

from solution_328 import Solution, ListNode


# Helper functions
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


class TestOddEvenList:
    def setup_method(self):
        """Setup that runs before each test method"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case: [1,2,3,4,5] -> [1,3,5,2,4]"""
        head = create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.oddEvenList(head)
        assert linked_list_to_list(result) == [1, 3, 5, 2, 4]

    def test_example_2(self):
        """Test case: [2,1,3,5,6,4,7] -> [2,3,6,7,1,5,4]"""
        head = create_linked_list([2, 1, 3, 5, 6, 4, 7])
        result = self.solution.oddEvenList(head)
        assert linked_list_to_list(result) == [2, 3, 6, 7, 1, 5, 4]

    def test_empty_list(self):
        """Test case: Empty list"""
        head = create_linked_list([])
        result = self.solution.oddEvenList(head)
        assert linked_list_to_list(result) == []

    def test_single_element(self):
        """Test case: Single element [1]"""
        head = create_linked_list([1])
        result = self.solution.oddEvenList(head)
        assert linked_list_to_list(result) == [1]

    def test_two_elements(self):
        """Test case: Two elements [1,2]"""
        head = create_linked_list([1, 2])
        result = self.solution.oddEvenList(head)
        assert linked_list_to_list(result) == [1, 2]

    def test_three_elements(self):
        """Test case: Three elements [1,2,3]"""
        head = create_linked_list([1, 2, 3])
        result = self.solution.oddEvenList(head)
        assert linked_list_to_list(result) == [1, 3, 2]


if __name__ == "__main__":
    # Allow running with: python test_328.py
    pytest.main([__file__, "-v"])
