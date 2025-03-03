class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            if c.isdigit() or c.isalpha():
                arr.append(c.lower())

        left,right = 0,len(arr)-1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1

        return True

    def followUp(self,s):
        left,right = 0, len(s) -1
        while left < right:
            while left < right and not s[left].isdigit() and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isdigit() and not s[right].isalpha():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True