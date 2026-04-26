class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)==0 and len(nums2) ==1:
            return nums2[0]
        if len(nums1)==1 and len(nums2) ==0:
            return nums1[0]
        result =0.0
        nums1.extend(nums2)
        nums1.sort()
        print(len(nums1))
        index = int(len(nums1)/2)
        if len(nums1) % 2 == 0:
            result = (nums1[index]+ nums1[index-1])/2
        else:
            # index = index
            result = (nums1[index])
        
        return result



        