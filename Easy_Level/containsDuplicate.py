# leet code 217  
# containsDuplicate

### there is three waies to solve this problem 

## 1 use two for loop

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:

    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
          return True

        return False
        
        # time complexity O(n^2)
        # space complexity O(1)


## 2 Sorting for the list 

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:

    nums.sort()
    for i in range (1 ,len(nums)):
      if nums[i] == nums[i - 1]:
        return True

      return False 

      # time complexity O(nl og n)
       # space complexity O(1) or O(n) depending on the sorting algorithm



## Hash Set
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Use set() to create an empty set
        for num in nums:
            if num in seen:  # Check if num is in the set
                return True
            seen.add(num)  # Add num to the set
        return False


    # time complexity O(n)
      # space complexity O(N)


## 4 Hash Set Length
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
