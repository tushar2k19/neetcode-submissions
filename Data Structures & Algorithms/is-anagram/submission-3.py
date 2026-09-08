class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1,mp2 = defaultdict(int), defaultdict(int)

        for x in s:
            mp1[x]+=1

        for x in t:
            mp2[x]+=1
        
        if mp1 == mp2:
            return True
        return False