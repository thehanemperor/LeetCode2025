class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one = m-1
        two = n -1
        i = m+n-1
        while one >= 0 and two >=0:
            if nums1[one] > nums2[two]:
                nums1[i] = nums1[one]
                one -= 1
            else:
                nums1[i] = nums2[two]
                two -= 1
            
            i -= 1

        while two >=0:
            nums1[i] = nums2[two]
            two -= 1
            i -= 1