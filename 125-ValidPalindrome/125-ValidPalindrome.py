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