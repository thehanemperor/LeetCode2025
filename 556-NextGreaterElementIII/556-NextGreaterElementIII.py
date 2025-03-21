// Last updated: 3/21/2025, 2:48:41 PM
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = []
        for num in str(n):
            arr.append(num)

        n = len(arr)
        i = n-2
        while i>=0:
            curr = int(arr[i])
            after = int(arr[i+1])
            if curr < after:
                break
            i -= 1

        if i <0:
            return -1

        left = i
        for right in range(n-1,-1,-1):
            if arr[right]>arr[left]:
                break
        arr[left],arr[right] = arr[right],arr[left]

        i = left + 1
        j = n -1
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1

        res = int("".join(arr))
        return res if res <= 2**31-1 else -1

        