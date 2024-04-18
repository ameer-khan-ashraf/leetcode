class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for ele in nums:
            if ele in x:
                return True
            x.add(ele)
        return False