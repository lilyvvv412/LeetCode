# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#一般来说如果需要删除头节点的话创建一个dummy node比较合适
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode(next=head)
        right=dummy
        for _ in range(n):
            right=right.next
        left=dummy
        while right.next:
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next
#time O(链表长度), space O(1)