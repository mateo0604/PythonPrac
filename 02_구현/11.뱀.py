import sys
from collections import deque
#보드 크기(N * N)
N = int(input())
#사과 개수
K = int(input())
#사과 위치
apples = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(K)]
#변환 횟수
L = int(input())
#변환 내용값 저장
direction = [sys.stdin.readline().strip().split() for _ in range(L)]
#딕셔너리로 변경(초 : 방향)
direction = {d[0]:d[1] for d in direction}
#보드판 생성
board = [[0]*N for _ in range(N)]
#보드판에 사과 추가
for x,y in apples:
    board[x-1][y-1]=1

#총 걸린시간
tot_sec = 0
#처음 위치
now_x,now_y = 0,0

#방향 변환값 저장 변수(진행방향 알기 위함)
q = deque([(0,1),(1,0),(0,-1),(-1,0)])    

#방향 변환 함수
def changeDirect(c):
    global q
    if c == 'D':
        q.rotate(-1)
    elif c == 'L':
        q.rotate(1)
    return q[0]

#방향(처음은 오른쪽 방향 이므로 열이 1씩 증가)
x,y = 0,1
#몸 길이
snake_len = 1
#뱀(몸)이 있는 좌표 저장 
snake_x_y = deque([(0,0)])
#board 처음 snake흔적 남기기
board[0][0] = -1
while True:
    tot_sec += 1
    now_x,now_y = now_x+x,now_y+y
    # 벽만나면 종료(1.보드 길이 초과 , 2.자기 몸 닿음)
    if now_x >= N or now_x <0 or now_y >= N or now_y <0 or board[now_x][now_y] == -1:
        break
    # 뱀 현재 좌표 추가
    snake_x_y.append((now_x,now_y))

    #사과만나면 
    if board[now_x][now_y] == 1:
        #뱀 길이 증가
        snake_len += 1
        
    #사과 안만나면 뱀 처음 좌표 0으로 만들기
    else:
        i,j = snake_x_y.popleft()
        board[i][j] = 0
    #흔적 남기기
    board[now_x][now_y] = -1

    if str(tot_sec) in direction.keys():
        x,y = changeDirect(direction[str(tot_sec)])
print(tot_sec)   