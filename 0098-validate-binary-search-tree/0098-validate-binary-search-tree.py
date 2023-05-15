# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        out=[]
        self.ordering(root,out)
        print(out)
        for i in range(0,len(out)-1):
            if (out[i+1] <= out[i]):
                return False
        
        return True
    
    def ordering(self,root,output):
        if not root:
            return 
        
        self.ordering(root.left,output)
        output.append(root.val)
        self.ordering(root.right,output)