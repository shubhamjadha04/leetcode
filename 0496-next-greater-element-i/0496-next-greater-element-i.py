class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []

        for i in range(len(nums1)):

            index = nums2.index(nums1[i])

            found = False

            for j in range(index+1,len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    found = True
                    break
            

            if not found:
                res.append(-1)

        return res