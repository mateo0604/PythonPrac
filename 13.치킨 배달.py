import sys
n,m = map(int,input().split())
maps = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
house = list()
chicken = list()
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append((i,j))
        # 치킨집인 경우
        if maps[i][j] == 2 :
            chicken.append([i,j,0])
for val in chicken:
    ch_x,ch_y,tot = val
    h_x,h_y = min(house,key = lambda x : abs(x[0]-ch_x) + abs(x[1]-ch_y))
    val[2] +=  abs(ch_x-h_x) + abs(ch_y-h_y)
# 치킨집 거리 정렬(거리합 기준)
chicken.sort(key = lambda x : x[2])

# 최대 개수 M일때까지     
while len(chicken) > m:
    chicken.pop()

#결과값 
result = 0
while True:
    prev_val = 0
    after_val = 0
    # 빼기 전 합 
    for h in house:
        h_x,h_y = h
        ch_x,ch_y,_ = min(chicken,key=lambda x : abs(h_x-x[0])+abs(h_y-x[1]))
        prev_val+= abs(ch_x-h_x) + abs(ch_y-h_y)

    if len(chicken) < 2:
        result = prev_val
        break

    chicken.pop()
    # 뺀 후 합
    for h in house:
        h_x,h_y = h
        ch_x,ch_y,_ = min(chicken,key=lambda x : abs(h_x-x[0])+abs(h_y-x[1]))
        after_val += abs(ch_x-h_x) + abs(ch_y-h_y)

    # 뺀 후 합이 빼기 전보다 크면 break
    if prev_val < after_val:
        result = prev_val
        break
print(result)