# 1.two sum

# Input: nums = [3,2,4], target = 6
#   Output: [1,2]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     for i in range(len(nums)):
         for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            return []
        # time O(n^2) 
        # space O(1)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #valure -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[n] = i
            
            # time O(n)
            # space O(n)
                            
