class Solution:
    def ispalin(self, s: str) -> bool:
        print(s)
        l = 0
        r = len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True


    #ababcbcaba  len = n-2(l) -1
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<=r:
            print (l,r)
            if s[l]==s[r]:
                l +=1
                r-=1
            else:
                print(l, r, s[l:r-1], s[l+1:r])
                # print()
                if self.ispalin(s[l:r]) or self.ispalin(s[l+1: r+1]):
                    return True
                else:
                    return False
        return True


        