def solution(N,M,balls):
    cnt = 0
    for i in range(N-1):
        cnt += N - (i+1) - balls[i+1:].count(balls[i])
    
    return cnt
