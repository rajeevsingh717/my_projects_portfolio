# 31. Next Permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def permute(choice, path):
            if not choice:
                if path not in result:
                    result.append(path)
            for i in range(len(choice)):
                newchoice = choice[:i] + choice[i+1:]
                permute(newchoice , path + [choice[i]])
        
        result = []
        permute(nums, [])
        result.sort()
        print(result)
        for i in range(0, len(result)):
            if result[i] == nums:
                if i==len(result)-1:
                    nums[:] = result[0]
                else:
                    nums[:] = result[i+1]
                break
         
        
