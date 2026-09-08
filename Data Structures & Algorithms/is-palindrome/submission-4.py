class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        l,r = 0,len(s)-1
        while l<=r:
            if not((ord(s[l]) >= ord('a') and ord(s[l]) <= ord('z')) or (ord(s[l]) >= ord('A') and ord(s[l]) <= ord('Z')) or (ord(s[l]) >= ord('0') and ord(s[l]) <= ord('9'))):
                l+=1
            elif not((ord(s[r]) >= ord('a') and ord(s[r]) <= ord('z')) or (ord(s[r]) >= ord('A') and ord(s[r]) <= ord('Z')) or (ord(s[r]) >= ord('0') and ord(s[r]) <= ord('9'))):
                r-=1
            else:
                if s[l].lower()!=s[r].lower():
                    return False
                l+=1
                r-=1
            print(l,r)
        return True



        