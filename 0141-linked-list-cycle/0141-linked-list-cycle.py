# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur=head
        l=list()
        while cur:
            if cur in l :
                return True
            else:
                l.append(cur)
                cur=cur.next
        return False
        