class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        out = []
        for i in range(len(arrays[0])):
            count = 0
            for j in range(1, len(arrays)):
                if arrays[0][i] in arrays[j]:
                    count += 1
            if count == len(arrays)-1:
                out.append(arrays[0][i])
        return out