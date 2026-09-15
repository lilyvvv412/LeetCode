# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self,head:Optional[ListNode])->Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def reverseList(self,head:Optional[ListNode])->Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid=self.middleNode(head)
        head2=self.reverseList(mid) #从中点开始反转
        #每轮把head2插到head后面,然后都往后走
        while head2.next:
            nxt=head.next
            nxt2=head2.next
            head.next=head2
            head2.next=nxt
            head=nxt
            head2=nxt2
#time O(n), space O(1)