class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n %2 ==0:
            return (self.find(nums1,0,len(nums1)-1, nums2, 0, len(nums2)-1, n//2-1) + self.find(nums1,0,len(nums1)-1, nums2, 0, len(nums2)-1, n//2))/2
        else:
            return self.find(nums1,0,len(nums1)-1, nums2, 0, len(nums2)-1, n//2)

    def find(self, nums1, start1,end1, nums2,start2,end2,k):
        if start1 > end1:
            return nums2[k-start1]

        if start2> end2:
            return nums1[k-start2]

        i,j = (start1 + end1)//2, (start2+end2) //2
        
        if i + j <k:
            if nums1[i] > nums2[j]:
                return self.find(nums1,start1,end1,nums2,j+1,end2,k)
            else:
                return self.find(nums1,i+1,end1,nums2,start2,end2,k)
        else:
            if nums1[i] > nums2[j]:
                return self.find(nums1,start1,i-1,nums2,start2,end2,k)
            else:
                return self.find(nums1,start1,end1,nums2,start2,j-1,k)