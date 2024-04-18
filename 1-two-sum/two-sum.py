class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for count,val in enumerate(nums):
            diff = target - val
            if diff in dict:
                return [count, dict[diff]]
            dict[val] = count