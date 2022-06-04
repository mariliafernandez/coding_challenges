def make_bricks(small, big, goal):

    missing_length = {s: goal - s for s in range(small+1)}
    
    for missing_for_goal in missing_length.values():
        if missing_for_goal % 5 == 0 and missing_for_goal <= 5*big:
            print(f'{goal-missing_for_goal} SMALL + {missing_for_goal//5} BIG = {goal}')
            return True
    return False