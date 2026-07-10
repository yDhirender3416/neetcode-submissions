class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff not in indices:
                indices[n]=i
            else:
                return [indices[diff],i]
        return