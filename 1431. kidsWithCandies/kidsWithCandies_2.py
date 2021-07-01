class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        for i in range(len(candies)):
            out.append(bool(candies[i] + extraCandies >= max(candies)))
        return out