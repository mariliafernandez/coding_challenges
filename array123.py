def array123(nums):
    previous = None
    entered_sequence = False

    for num in nums:

        if num == 2 and previous == 1:
            entered_sequence = True

        elif num == 3 and previous == 2 and entered_sequence:
            return True
        
        previous = num
    return False