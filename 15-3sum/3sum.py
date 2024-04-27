class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i,n in enumerate(nums):
            # check to see if previous value is same as current value. skip if same to have distinct triplets
            if i>0 and n == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1

            while l<r:
                sum = n + nums [l] + nums [r]
                    
                if sum<0:
                    l +=1
                elif sum > 0:
                    r -=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    # check to see if next value is same as current value. skip if same to have distinct triplets
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res