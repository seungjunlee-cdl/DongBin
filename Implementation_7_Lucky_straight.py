def solution(N):
    left_sc = list(map(int,N[0:int(len(N)/2)]))
    right_sc = list(map(int,N[int(len(N)/2):]))
    if sum(left_sc) == sum(right_sc):
        print("LUCKY")
    else:
        print("READY")
