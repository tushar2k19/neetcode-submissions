class Solution:
    def valid(self, s: chr):
        if (ord(s) >= ord('A') and ord(s) <= ord('Z')):
            return True
        if (ord(s) >= ord('a') and ord(s) <= ord('z')):
            return True
        if (ord(s) >= ord('0') and ord(s) <= ord('9')):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        i,j = 0, len(s)-1
        while i<j:
            if not self.valid(s[i]):
                i+=1
                continue

            if not self.valid(s[j]):
                j-=1
                continue

            if s[i]!=s[j]:
                print(s[i], s[j])
                return False
            i+=1
            j-=1

        return True
        