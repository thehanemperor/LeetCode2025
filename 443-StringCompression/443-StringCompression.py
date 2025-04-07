# Last updated: 4/7/2025, 2:34:33 AM
class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        while right < len(chars):
            groupLength = 1
            while right +groupLength < len(chars) and chars[right] == chars[right+groupLength]:
                groupLength += 1

            chars[left] = chars[right]
            
            left += 1
            if groupLength > 1:
                tmpStr = str(groupLength)
                for t in tmpStr:
                    chars[left] = t
                    left += 1
            right += groupLength

        return left
             