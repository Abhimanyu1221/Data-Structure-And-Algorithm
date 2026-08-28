class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 ={}
        dict2={}
        if len(s)!=len(t):
            return False

        for ch in s :
            dict1[ch]=dict1.get(ch,0)+1
        for ch in t :
            dict2[ch]=dict2.get(ch,0)+1
        

        for ch in dict1:
            if dict1.get(ch) != dict2.get(ch):
                return False
        return True