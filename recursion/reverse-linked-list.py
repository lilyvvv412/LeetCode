# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr: #只要curr还不是None
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
#time O(n)取决于循环次数,节点个数; space O(1)