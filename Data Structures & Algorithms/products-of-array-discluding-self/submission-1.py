class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product, zero_cnt = 1, 0
        
        for i in range(len(nums)):
            if nums[i]==0:
                zero_cnt+=1
                if zero_cnt==1:
                    zero_index=i
                continue
            else:
                product*=nums[i]
        
        output = [0]*len(nums)
        
        if zero_cnt>1:
            return output
        elif zero_cnt==1:
            output[zero_index]=product
            return output
        else:
            for j in range(len(nums)):
                output[j]=product//nums[j]
        return output