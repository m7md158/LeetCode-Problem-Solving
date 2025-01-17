class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        for i in range(n):
            rightMax = -1
            for j in range(i+1, n):
                rightMax = max(rightMax, arr[j])
            ans[i] = rightMax
        return ans
    
    # time O(n^2)
    # space O(1)
    # limit time 


# update the list from the last 
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans

    # time O(n)
    # space O(1)
