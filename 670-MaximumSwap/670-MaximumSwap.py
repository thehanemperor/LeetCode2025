// Last updated: 3/21/2025, 3:24:33 PM
class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = []
        for n in str(num):
            arr.append(n)
        n = len(arr)
        maxRight = [n-1] * n
        for i in range(n-2,-1,-1):
            if arr[i] > arr[maxRight[i+1]]:
                maxRight[i] = i
            else:
                maxRight[i] = maxRight[i+1]

        for i in range(n):
            if arr[i] < arr[maxRight[i]]:
                arr[i], arr[maxRight[i]] = arr[maxRight[i]], arr[i]
                return int("".join(arr))

        return num
            
        