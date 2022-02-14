def solution(food_times,k):
    iter = 0
    for i in range(k):
        while (food_times[iter] == 0) and (sum(food_times) != 0):
            iter = (iter+1)%(len(food_times))
        food_times[iter] -= 1
        iter = (iter+1)%(len(food_times))

    while (food_times[iter] == 0) and (sum(food_times) != 0):
        iter = (iter+1)%(len(food_times))
        
    if sum(food_times) == 0:
        return -1
    
    return iter+1
