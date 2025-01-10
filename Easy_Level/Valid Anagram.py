###  242. Valid Anagram

## the first way
# sorted two strings
# if they are equal as the characters arangment or not 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
    # time O(nlogn + mlogm)
    # space O(1) or O(n+m) depending on the sorting algorithm
    
    
## the second way
# hash table
# stored in a hash table each caracter and its counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT


    # Input: s = "anagram", t = "nagaram"
    
    # countS = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
    # countT = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
    
    # time O(n + m)
    # space O(1) 
    
