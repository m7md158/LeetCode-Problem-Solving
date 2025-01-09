# leet code 217


# there is three waies to solve this problem 

## 1 use two for loop

class Solution:
  def hassDuplicate(self, nums: List[int]) -> bool:

    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
          return True

        return False
        
        # time complexity O(n^2)
        # space complexity O(1)


## 2 Sorting for the list 

class Solution:
  def hassDuplicate(self, nums: List[int]) -> bool:

    nums.sort()
    for i in range (1 ,len(nums)):
      if nums[i] == nums[i - 1]:
        return True

      return False 

      # time complexity O(nl og n)
       # space complexity O(1) or O(n) depending on the sorting algorithm



## Hash Set
class Solution:
  def hassDuplicate(self, nums: List[int]) -> bool:
    seen = Set()
    for num in nums:
      if nums in seen:
        return True
      #else
      seen.add(num)
    return False 

    # time complexity O(n)
      # space complexity O(N)

