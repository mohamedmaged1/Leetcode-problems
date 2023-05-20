class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out=[]
        
        for i,n in enumerate (nums):
            if (i>0 and n == nums[i-1]):
                continue
            
            left,right=i+1, len(nums)-1
            
            while (left<right):
                target = n + nums[left] +nums[right]
                
                if (target > 0):
                    right-=1
                
                elif(target<0):
                    left+=1
                
                else :
                    out.append([n,nums[left] ,nums[right]])
                    left += 1 
                    while (nums[left]==nums[left-1] and left <right ):
                        left+=1

        return out
        
                
        
        
        
        
        