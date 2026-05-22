class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 ={}
        for x in s:
            dict1[x] = dict1.get(x,0)+1
        print(dict1)
        
        for y in t:
            dict2[y] = dict2.get(y,0)+1
        print(dict2)
        return dict1==dict2
