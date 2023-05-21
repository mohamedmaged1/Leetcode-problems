class Solution(object):
    def lengthOfLongestSubstring(self, s):

        seen = set()
        left=0
        longest=0
        for r in range(len(s)):
            while s[r] in seen :
                seen.remove(s[left])
                left+=1
            seen.add(s[r])
            longest=max(longest,r-left+1)
            
        return longest
            
        
        
      