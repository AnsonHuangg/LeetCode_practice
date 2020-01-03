# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        
        node1.next = node2
        node2.next = node3
        printList(node1)
        
        
print(Solution().addTwoNumbers([2,4,3],[5,6,4]))

