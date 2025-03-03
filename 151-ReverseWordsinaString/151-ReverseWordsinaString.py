class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        left = 0
        right = n-1
        while left < n and s[left] == " ":
            left += 1

        while right >= 0 and s[right] == " ":
            right -= 1

        arr = []
        for i in range(left,right+1):
            if i-1 >=0 and s[i] == " " and s[i-1]== " ":
                continue
            arr.append(s[i])
        self.reverse(0,len(arr)-1, arr)
        left = 0
        for i in range(len(arr)):
            if arr[i] == " ":
                self.reverse(left,i-1,arr)
                left = i +1

        self.reverse(left,len(arr)-1,arr)
        return "".join(arr)
                
        
    def reverse(self,left,right,arr):
        while left <right:
            arr[left],arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        