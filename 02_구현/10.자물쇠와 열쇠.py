def solution():
    key = [[0,0,0],[1,0,0],[0,1,1]]
    lock = [[1,1,1],[1,1,0],[1,0,1]]
    N = len(lock)
    M = len(key)
    #1.똑같은 배열 9개 만들기
    new_lock = [[0]*(N*3) for _ in range(N*3)]

    #2.가운데 lock넣기
    for i in range(N):
        for j in range(N):
            new_lock[i+N][j+N] = lock[i][j]

    #3.key 각도 돌리기
    def rotate_key():
        nonlocal key
        n = len(key)
        m = len(key[0])
        new_key = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new_key[j][n-i-1]=key[i][j]
        return new_key
    
    #4.자물쇠 부분 맞는지 확인
    def check():
        nonlocal N,new_lock
        for i in range(N):
            for j in range(N):
                if new_lock[N+i][N+j] != 1:
                    return False
        return True
    #5.각도를 90도씩 4번돌려 확인
    for _ in range(4):
        key = rotate_key()
        for i in range(1,N*2):
            for j in range(1,N*2):
                #6. key를 new_lock에 넣기
                for x in range(M):
                    for y in range(M):
                        new_lock[i+x][j+y] += key[x][y]
                #7. 자물쇠 위치가 모든 칸이 1인지 확인
                if check():
                    return 'true'
                #8. 아까 더한 key 다시 빼기
                for x in range(M):
                    for y in range(M):
                        new_lock[i+x][j+y] -= key[x][y]
    return 'false'

print(solution())