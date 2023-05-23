class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res,left=0,0
        seen={}
        for r in range(len(s)):
            seen[s[r]]=1+seen.get(s[r],0)
            if (r-left+1)- max(seen.values()) >k:
                seen[s[left]]-=1
                left+=1
            
            res=max(res,r-left+1)
        
        return res
                
        
        
        