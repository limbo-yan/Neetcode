class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(string: str):
            l = 0
            r = len(string) - 1
            while l < r:
                if string[l] == string[r]:
                    l += 1
                    r -= 1
                else:
                    return False
                
            return True
        
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
        
        return True
        