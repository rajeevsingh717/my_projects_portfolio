# 15. 3Sum
class Solution(object):
    def threeSum(self, lst):
        lst.sort()
        res=[]
        for i in range(0,len(lst)-2):
            left = i+1
            right = len(lst)-1
            while left < right:
                curr_sum = lst[i]+lst[left]+lst[right]
                if curr_sum==0:
                    if [lst[i],lst[left],lst[right]] not in res:
                        res.append([lst[i],lst[left],lst[right]])
                    left +=1
                    right -=1
                elif curr_sum<0:
                    left +=1
                elif curr_sum>0:
                    right -=1
        return res	
        
