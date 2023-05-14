class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums)==0):return 0
        l=sorted(list(set(nums)))
        a=[]
        out=1
        print(l)
        for i in range(0,len(l)-1):
            if (l[i+1] -l[i] ==1):
                out+=1
            else:
                a.append(out)
                out=1
        a.append(out)
        return max(a)
        