class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for x in strs:
            s = tuple(sorted(x))   # or ''.join(sorted(x)) and then use this as a key in map
                                   # key = ''.join(sorted(x))
                                   # mp[key].append(x)
            mp[s].append(x)
        
        ans = []
        for x in mp.values():
            ans.append(x)
        return ans

    

