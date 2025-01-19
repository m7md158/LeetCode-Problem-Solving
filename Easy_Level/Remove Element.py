# the first way ==> create a temp array
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
            
        for i in range(len(nums)):
            nums[i] = tmp[i]  # update the nums list
        return len(tmp)
                
            
    # time O(n)
    # space O(n)

    
# the second way  
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        
        

    # time O(n)
    # space O(1)
