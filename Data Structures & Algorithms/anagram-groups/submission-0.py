class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        while len(strs)>0:
            current_word=strs.pop(0)
            current_group=[current_word]
            
            j=0
            while j<len(strs):
                if sorted(current_word)==sorted(strs[j]):
                    current_group.append(strs.pop(j))
                else:
                    j+=1
            
            output.append(current_group)
        return output


        
