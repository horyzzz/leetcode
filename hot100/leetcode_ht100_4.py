from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        def getKthelement(k):
            p1, p2 = 0, 0
            while True:
                if p1 == m:
                    return nums2[p2 + k - 1]
                if p2 == n:
                    return nums1[p1 + k - 1]
                if k == 1:
                    return min(nums1[p1], nums2[p2])

                newindex1 = min(p1 + k // 2 - 1, m - 1)
                newindex2 = min(p2 + k // 2 - 1, n - 1)
                if nums1[newindex1] > nums2[newindex2]:
                    k -= newindex2 - p2 + 1
                    p2 = newindex2 + 1
                else:
                    k -= newindex1 - p1 + 1
                    p1 = newindex1 + 1
        
        if (m + n) % 2 == 1:
            return getKthelement((m + n + 1) // 2)
        else:
            return (getKthelement((m + n) // 2) + \
                        getKthelement((m + n) // 2 + 1)) / 2
         

sol = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(sol.findMedianSortedArrays(nums1, nums2))