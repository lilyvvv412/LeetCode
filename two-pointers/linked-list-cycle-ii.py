# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#找入口,环长=b+c,快慢相遇slow还没走完一整圈
#slow从相遇点出发,head从头节点出发,走c步后(每次只走一步),slow在入口,head到入口的距离也恰好是环长的倍数,两者必然会在入口相遇
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast is slow:
                while slow is not head:
                    slow=slow.next
                    head=head.next
                return slow
        return None
#time O(n), space O(1)