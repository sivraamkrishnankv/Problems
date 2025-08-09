from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot=0
        sd=defaultdict(int)
        c=0
        sd[0]=1
        for i in nums:
            tot+=i
            if tot-k in sd:
                c+=sd[tot-k]
            sd[tot]+=1
        return c