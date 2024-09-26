'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:
Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:
Input: head = []
Output: []

Constraints:
0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
'''

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        linkHead = head

        while linkHead != None:
            temp = linkHead.next
            linkHead.next = prev
            prev = linkHead
            linkHead = temp
        return prev

def printLinkedList(head: Optional[ListNode]) -> None:
    if head is None:
        print("The list is empty.")
    else:
        curr = head
        result = []
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(result))

def createLinkedList(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def runTests():
    sol = Solution()

    # Test 1: Reversing [1, 2, 3, 4, 5]
    head = createLinkedList([1, 2, 3, 4, 5])
    print("Original list:")
    printLinkedList(head)
    reversed_head = sol.reverseList(head)
    print("Reversed list:")
    printLinkedList(reversed_head)
    assert printLinkedList(reversed_head) == None

    # Test 2: Reversing [7, 8, 9]
    head = createLinkedList([7, 8, 9])
    print("\nOriginal list:")
    printLinkedList(head)
    reversed_head = sol.reverseList(head)
    print("Reversed list:")
    printLinkedList(reversed_head)
    assert printLinkedList(reversed_head) == None

    # Test 3: Empty list
    head = createLinkedList([])
    print("\nOriginal list:")
    printLinkedList(head)
    reversed_head = sol.reverseList(head)
    print("Reversed list:")
    printLinkedList(reversed_head)
    assert reversed_head is None

    # Test 4: Single element list [42]
    head = createLinkedList([42])
    print("\nOriginal list:")
    printLinkedList(head)
    reversed_head = sol.reverseList(head)
    print("Reversed list:")
    printLinkedList(reversed_head)
    assert printLinkedList(reversed_head) == None



runTests()
