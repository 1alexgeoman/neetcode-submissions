class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potential = {}
        index = 0
        for number in nums:
            if number not in potential.keys():
                potential[number] = index
                if target-number in potential and potential[target-number] != potential[number]:
                    if potential[target-number]<number:
                        return [potential[target-number], potential[number]]
                    else:
                        return [potential[target-number], potential[number]]
            else:
                if potential[number]<index:
                        return [potential[number], index]
                else:
                    return [index, potential[number]]
            
            index+=1