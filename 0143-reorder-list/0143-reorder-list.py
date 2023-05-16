# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p=self.linkedtolist(head)
        mid=int(len(p)/2)
        if (len(p)%2 !=0):
            m1=p[0:mid+1]
            m2=p[mid+1:]
        else:
            m1=p[0:mid]
            m2=p[mid:]
        l=[]
        for i in range(1,mid+1):
            try :
                l.append(m1[i-1])
                l.append(m2[-i])
            except:
                l.append(m1[i-1])
                
        if (len(p)%2 !=0):
            l.append(m1[-1])
        
        print(l)
        self.head = ListNode(l[0])
        curr = head
    
        for val in l[1:]:
            curr.next = ListNode(val)
            curr = curr.next
    
    
        
    def linkedtolist (self,head):
        cur=head
        a=[]
        while cur:
            a.append(cur.val)
            
            cur=cur.next
        return a        