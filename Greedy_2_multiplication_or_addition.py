def solution(S):
    largest = int(S[0])
    for i in range(len(S)-1):
        if (i==0) and (largest == 0):
            largest += int(S[1])
        elif int(S[i+1])==0:
            continue
        else:
            largest *= int(S[i+1])

    return largest
