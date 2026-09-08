class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        
        ans = ""
        for i in range(len(strs[0])):
            print("i = ", i)
            for x in strs:
               
                if i >= len(x):
                    return ans
                if strs[0][i] != x[i]:
                    return ans
            ans+=strs[0][i]
        
        return ans
    
        