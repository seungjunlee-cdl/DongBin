import math

def solution(S):
    cnt = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            cnt += 1

    return math.ceil(cnt/2)
