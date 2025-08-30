# Leecode question number 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index= {}
        for i, num in enumerate(nums):
            total= target - num
            if total in num_index:
                return[num_index[total], i]
            num_index[num]= i
