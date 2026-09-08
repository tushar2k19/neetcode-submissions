class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for i,x in enumerate(strs):
            str = ''.join(sorted(x))
            mp[str] = mp.get(str,[])
            mp[str].append(i)
            print(mp.items())
        ans = []

        for x in mp.values():
            tmp = []
            for y in x:
                tmp.append(strs[y])
            if len(tmp)!=0:
                ans.append(tmp)
        print(ans)
        return ans

