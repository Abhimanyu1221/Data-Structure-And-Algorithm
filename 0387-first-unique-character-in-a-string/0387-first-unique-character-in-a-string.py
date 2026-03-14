class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_dict = {}
        for ch in s:
            if ch not in freq_dict:
                freq_dict[ch] = 1
            else:
                count = freq_dict.get(ch)
                freq_dict[ch] = count+1
        for key,val in freq_dict.items():
            if val == 1:
                return s.index(key)
        
        return -1

        