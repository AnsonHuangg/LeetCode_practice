class Key_find:
    def get_key(self, dict, value):
        return [k for k, v in dict.items() if v == value]
        
class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        dict = {}
        for i in range(len(arrays)):
            for j in range(len(arrays[i])):
                if dict.get(arrays[i][j])==None:
                    dict[arrays[i][j]] = 1
                else:
                    dict[arrays[i][j]] = dict.get(arrays[i][j])+1
        
        return Key_find().get_key(dict, len(arrays))