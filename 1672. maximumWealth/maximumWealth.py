class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = []
        for i in range(len(accounts)):
            temp = 0
            for j in range(len(accounts[i])):
                temp = temp + accounts[i][j]
            sum.append(temp)
        return max(sum)