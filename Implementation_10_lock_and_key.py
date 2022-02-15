def rotated(arr):
    list_of_tuples = zip(*arr[::-1])
    return [list(elem) for elem in list_of_tuples]

def solution(key, lock):
    M = len(key)
    N = len(lock)

    for i in range(N+M-1):
        for j in range(N+M-1):
            for r in range(4):
                lock_exp = [[0]*(N+2*M-2) for _ in range(N+2*M-2)]

                for a in range(N):
                    for b in range(N):
                        lock_exp[a+M-1][b+M-1] = lock[a][b]

                if r==0:
                    key_rot = key
                else:
                    key_rot = rotated(key_rot)

                for k in range(M):
                    for l in range(M):
                        lock_exp[i+k][j+l] += key_rot[k][l]

                d = 1
                for m in range(M-1,M-1+N):
                    for n in range(M-1,M-1+N):
                        d *= lock_exp[m][n]

                if d==1:
                    return True

    return False
