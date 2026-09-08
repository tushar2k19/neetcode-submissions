class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)

        for x in strs:
            arr = [0]*26
            for i in x:
                arr[ord(i)-ord('a')]+=1
            # mp[arr].append(x)
            # arrays ain't hashable in python so they can't be used as keys.
            # instead use tuple which is hashable
            mp[tuple(arr)].append(x)
        ans = []
        for x in mp.values():
            ans.append(x)

        return ans

