# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: #只反转left到right这一段
        dummy=ListNode(next=head)
        p0=dummy
        for _ in range(left-1):
            p0=p0.next #p0往后走left-1步
        prev=None
        curr=p0.next
        for _ in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        p0.next.next=curr #因为 curr.next 会马上被你改掉，所以必须先存；但 p0.next 在反转循环里从来没有被改，所以它一直还指着原来的节点
        p0.next=prev
        return dummy.next