class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)

        for x in strs:
            arr = [0]*26
            for i in x:
                arr[ord(i)-ord('a')]+=1
            # mp[arr].append(x)
            mp[tuple(arr)].append(x)
        ans = []
        for x in mp.values():
            ans.append(x)

        return ans

