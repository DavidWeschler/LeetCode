'''
You are given the heads of two sorted linked lists 'list1' and 'list2'.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.

Example 1:
1 -> 2 -> 4
1 -> 3 -> 5
-----------
1 -> 1 -> 2 -> 3 -> 4 -> 5

Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []

Constraints:
0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next


def printList(list: Optional[ListNode]):
    vals = []
    head = list
    while head:
        vals.append(str(head.val))
        head = head.next
    print('->'.join(vals))

def createLinkedList(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == '__main__':
    sol = Solution()

    # Test case 1: Merging [1, 3, 5] and [2, 4, 6]
    list1 = createLinkedList([1, 3, 5])
    list2 = createLinkedList([2, 4, 6])
    merged = sol.mergeTwoLists(list1, list2)
    print("Merged list:")
    printList(merged)

    # Test case 2: Merging [1, 2, 4] and [1, 3, 4]
    list1 = createLinkedList([1, 2, 4])
    list2 = createLinkedList([1, 3, 4])
    merged = sol.mergeTwoLists(list1, list2)
    print("Merged list:")
    printList(merged)

    # Test case 3: Merging an empty list with a non-empty list
    list1 = createLinkedList([])
    list2 = createLinkedList([0])
    merged = sol.mergeTwoLists(list1, list2)
    print("Merged list:")
    printList(merged)

    list1 = createLinkedList([5])
    list2 = createLinkedList([1, 2, 4])
    merged = sol.mergeTwoLists(list1, list2)
    print("Merged list:")
    printList(merged)