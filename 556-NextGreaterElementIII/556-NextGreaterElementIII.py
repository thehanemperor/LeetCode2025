class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = []
        while n >0:
            arr.append(n%10)
            n = n //10
        arr.reverse()

        right = len(arr)-1
        found = False
        while right>=0:
            if right +1 < len(arr) and arr[right] < arr[right+1]:
                found = True
                break
            right -= 1
        
        if not found:
            return -1

        for i in range(len(arr)-1,right,-1):
            if arr[i] > arr[right]:
                arr[i],arr[right] = arr[right],arr[i]
                break

        left = right + 1
        right = len(arr) -1
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1

        power = len(arr)-1
        res = 0
        for num in arr:
            res += num* 10**power
            power -= 1
        if res >= 2**31:
            return -1
        return res


        

        