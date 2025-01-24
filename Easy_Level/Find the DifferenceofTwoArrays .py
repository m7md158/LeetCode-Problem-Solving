class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashSet1, hashSet2 = set(nums1) , set(nums2)
        res1 , res2 = [], []

        for num in hashSet1:
            if num not in hashSet2:
                res1.append(num)
        
        for num in hashSet2:
            if num not in hashSet1:
                res2.append(num)


# the second way
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashSet1, hashSet2 = set(nums1) , set(nums2)
        res1 , res2 = [], []
        
        return [list(hashSet1 - hashSet2),list(hashSet2 - hashSet1 )]
