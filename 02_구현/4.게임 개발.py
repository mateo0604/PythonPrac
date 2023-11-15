import sys
n,m = map(int,input().split())
a,b,d = map(int,input().split())
maps = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
direct = {0:(-1,0),
          1:(0,1),
          2:(1,0),
          3:(0,-1)}

# 처음 방향 저장
start_d = d
# 방문 횟수
result = 1
print(maps)
while True:
    # 회전한 곳 방향 설정
    turn_d = (d+3) % 4
    # 움직일 거리
    mx,my = direct[turn_d]
    print(f"현재 a,b = {a},{b} / mx,my = {mx},{my} / start 방향 : {start_d} / 바라보는 방향 : {turn_d}")
    # 원점이라면 뒤로 back
    if start_d == turn_d:
        bx,by = direct[d]
        a,b = a-bx,b-by
        # 바다라면 break
        if maps[a][b] == 1:
            break
        start_d = d
        # 방향 유지
        continue
    # 안가봇곳이라면 움직이고 위치 바꿈
    elif maps[a+mx][b+my] == 0 :
        maps[a][b] = 2
        a,b = a+mx,b+my
        d = turn_d
        start_d = d
        result += 1
    # 바다거나 방문한 곳이라면 턴만
    else:
        d = turn_d
print(result)
        