# Last updated: 3/24/2025, 1:55:15 AM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) -1
        while left <= right:
            mid = left + (right- left) //2
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            else:
                right = mid -1

        if left >= len(letters):
            return letters[0]
        return letters[left]