from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pcount=defaultdict(int)
        scount=defaultdict(int)
        start=0
        ans=[]
        for i in p:
            pcount[i]+=1
        for i in range(len(s)):
            scount[s[i]]+=1
            if i-start+1==len(p):
                if pcount==scount:
                    ans.append(start)
                scount[s[start]]-=1
                if scount[s[start]]==0:
                    del scount[s[start]]
                start+=1
        return ans