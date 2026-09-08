class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}

        for x in s:
            mp1[x] = mp1.get(x, 0) + 1
        for x in t:
            mp2[x] = mp2.get(x,0) + 1
            
        if mp1==mp2:
            return True
        else:
            return False