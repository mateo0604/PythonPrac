import sys
from itertools import combinations
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
            chicken.append([i,j])
result = int(1e5)
for com in list(combinations(chicken,m)):
    h_sum = 0
    for h in house:
        hx,hy = h
        h_sum += min(abs(c[0]-hx) + abs(c[1]-hy) for c in com)
    if result > h_sum:
        result = h_sum
print(result)