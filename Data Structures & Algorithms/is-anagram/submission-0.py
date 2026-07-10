class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list1=list(s)
        char_list1.sort()
        char_list2=list(t)
        char_list2.sort()
        if(char_list1==char_list2):
            return True
        return False