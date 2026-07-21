class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices={}
        for i,n in enumerate(numbers):
            diff=target-n
            if diff not in indices:
                indices[n]=i
            else:
                return [indices[diff]+1,i+1]