# Day-6

## 1. Jump Game<br>You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.<br>Return *True* if you can reach the last index, or *False* otherwise.
```
def canJump(nums):
    max_reach = 0  # Initialize the maximum reach
    for i, num in enumerate(nums):  # Loop through each index and its corresponding value
        if i > max_reach:  # If the current index is beyond the maximum reach
            return False  # We cannot proceed, return False
        max_reach = max(max_reach, i + num)  # Update max_reach
    return True  # If we finish the loop, we can reach the last index

nums = [3,2,1,0,4]
print(nums)
print(canJump(nums))

```
Output:-[3, 2, 1, 0, 4],<br>
False

## 2. Jump Game II <br>
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].<br>Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:<br>0 <= j <= nums[i] and
i + j < n  <br>Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

```
def jump(nums):  
   if len(nums) <= 1:  
      return 0  
   max_reach = nums[0]  
   step = nums[0]  
   jumps = 1  
   for i in range(1, len(nums)):  
      if i == len(nums) - 1:  
        return jumps  
      max_reach = max(max_reach, i + nums[i])  
      step -= 1  
      if step == 0:  
        jumps += 1  
        step = max_reach - i  
   return jumps

```
Output:-2