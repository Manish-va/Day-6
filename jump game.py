def Jump(nums):  
   max_reach = 0  
   for i in range(len(nums)):  
      if i > max_reach:  
        return False  
      max_reach = max(max_reach, i + nums[i])  
   return True
nums = [2,3,1,1,4]
#nums = [3,2,1,0,4]
print(Jump(nums))
