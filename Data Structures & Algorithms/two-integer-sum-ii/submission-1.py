class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x=0
        y = len(numbers)-1
        while x <= len(numbers)-1:
            if (target - numbers[x]) in numbers:
                while numbers[y] != (target - numbers[x]):
                    y-=1
                return[x+1,y+1]
            x+=1

