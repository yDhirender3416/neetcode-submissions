class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp=defaultdict(int)
        for n in nums:
            temp[n]+=1
        sorted_keys=sorted(temp.keys(), key=lambda x:temp[x], reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_keys[i])
        return res