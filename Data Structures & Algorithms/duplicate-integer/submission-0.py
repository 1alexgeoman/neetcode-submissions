class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = {}
        for x in nums:
            if x in found:
                
                return True
            found[x] = x
        return False