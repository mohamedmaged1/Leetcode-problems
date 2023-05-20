class Solution(object):
    def maxProfit(self, prices):
        if (len(prices)==0):
            return 0 

        else :
            l,r,ret=0,1,0

            while(r<len(prices)):
                
                if (prices[l] > prices[r]):
                    l=r
                
                else :
                    profit=prices[r]-prices[l]
                    ret=max(ret,profit)
                r+=1
            return ret
