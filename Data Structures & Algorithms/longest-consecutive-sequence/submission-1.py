class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq=set(nums)
        res=0
        for num in nums:
            if num-1 not in seq:
                streak, curr = 0, num
                while curr in seq:
                    streak+=1
                    curr+=1
                res=max(streak,res)
        return res