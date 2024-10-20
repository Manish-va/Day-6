def minimum_jumps(numbers):
    jumps = 0
    current_jump_end = 0
    farthest = 0
    # Iterate over the array until one step before the last element
    for i in range(len(numbers) - 1):
        # Update farthest position we can reach from the current position
        farthest = max(farthest, i + numbers[i])
        # If the current position is equal to the end of the current jump,
        # it means we've completed a jump and need to start a new one.
        # Hence, increase the jumps count
        if i == current_jump_end:
            jumps += 1
            # Start a new jump to the farthest position we can reach
            current_jump_end = farthest
    return jumps
numbers = [2, 3, 1, 1, 4]
print(minimum_jumps(numbers)) 

'''
Input: numbers = [2, 3, 1, 1, 4]
Variables:
jumps = 0: Counts the number of jumps made.
current_jump_end = 0: Marks the end of the current jump range.
farthest = 0: Keeps track of the farthest index we can reach.
Iteration Process
The function iterates through the array, stopping one index before the last, to determine the minimum jumps.
Iteration 0 (i = 0)
Current Value: numbers[0] = 2
Farthest Reach:
farthest = max(0, 0 + 2) = 2
Current Jump End:
current_jump_end = 0
Check if Jump Needed:
i (0) == current_jump_end (0): This condition is true, so we make a jump.
Increment Jumps: jumps = 1
Update Current Jump End: current_jump_end = farthest = 2
Iteration 1 (i = 1)
Current Value: numbers[1] = 3
Farthest Reach:
farthest = max(2, 1 + 3) = 4
Current Jump End:
current_jump_end = 2
Check if Jump Needed:
i (1) != current_jump_end (2): This condition is false, so no jump is made.
Iteration 2 (i = 2)
Current Value: numbers[2] = 1
Farthest Reach:
farthest = max(4, 2 + 1) = 4
Current Jump End:
current_jump_end = 2
Check if Jump Needed:
i (2) == current_jump_end (2): This condition is true, so we make another jump.
Increment Jumps: jumps = 2
Update Current Jump End: current_jump_end = farthest = 4
Iteration 3 (i = 3)
Current Value: numbers[3] = 1
Farthest Reach:
farthest = max(4, 3 + 1) = 4
Current Jump End:
current_jump_end = 4
Check if Jump Needed:
i (3) != current_jump_end (4): This condition is false, so no jump is made.
Conclusion
The loop ends because we have iterated through the array until one index before the last.
The function returns jumps, which is 2.
Summary of Jumps
First Jump:
Start at index 0, jump to index 2 (or 1).
Farther reach allows us to jump to index 4 in the next step.
Second Jump:
From index 2, jump to index 4.
Thus, the minimum number of jumps needed to reach the last index of [2, 3, 1, 1, 4] is 2.
'''