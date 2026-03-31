class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = 0
        for x in range (0,len(nums)):
            left = sum(nums[0:x])
            if x == 0:
                left = 0
            right = sum(nums[x+1:len(nums)])
            print("left",left,"right",right)
            if left == right:
                return x
        return -1