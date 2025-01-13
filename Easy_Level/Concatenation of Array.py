class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i)
          
        return nums+ans
    
    # time O(n)
    # space O(n)



class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans
    # time O(n)
    # space O(n)
