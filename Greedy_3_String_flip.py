import math

def solution(S):
    cnt = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            cnt += 1

    return math.ceil(cnt/2)

# testcase1 = '0001100'   return 1
# testcase1 = '11111'   return 0
# testcase1 = '00000001'   return 1
# testcase1 = '11001100110011000001'   return 4
# testcase1 = '11101101'   return 2
