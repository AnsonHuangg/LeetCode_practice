class Solution:
    def combinationSum(self, candidates, target):
        buf = target
        arr = []
        ans = []
        i = len(candidates)
        while sum(arr)<target:
            arr.append(candidates[-1])
        print(len(candidates))
        
        while i>0:
            print(arr)
            if sum(arr)>target:
                arr.pop()
                arr.pop()
                print("in if")
                i -= 1
                print("i=",i)
            elif sum(arr)<target:
                arr.append(candidates[-1])
                print("in elif")
            else:
                ans.append(arr)
                print("in else")
                arr.pop()
                i -= 1
        return ans





candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates,target))