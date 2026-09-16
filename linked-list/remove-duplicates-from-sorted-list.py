# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#sorted
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None: return head
        curr=head
        while curr.next:
            if curr.next.val==curr.val:
                curr.next=curr.next.next
            else: curr=curr.next #移到下个节点
        return head
#O(n), O(1)