def solution(N,M,balls):
    cnt = 0
    for i in range(N-1):
        cnt += N - (i+1) - balls[i+1:].count(balls[i])
    
    return cnt

# testcase1 => N = 5, M = 3, balls = [1,3,2,3,2]   return 8
# testcase2 => N = 8, M = 5, balls = [1,5,4,3,2,4,5,2]   return 25
