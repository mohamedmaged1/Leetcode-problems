# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out=[]
        self.ordering(root,out)
        
        return out[k-1]
    
    def ordering(self,root,output):
        if not root :
            return
        
        self.ordering(root.left,output)
        output.append(root.val)
        self.ordering(root.right,output)