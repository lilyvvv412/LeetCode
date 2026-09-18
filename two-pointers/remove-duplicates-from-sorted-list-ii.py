# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#sorted
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode(next=head)
        curr=dummy
        while curr.next and curr.next.next:
            val=curr.next.val
            if curr.next.next.val==val: #删掉所有等于val的节点
                while curr.next and curr.next.val==val:
                    curr.next=curr.next.next
            else: curr=curr.next
        return dummy.next
#time O(n), space O(1)