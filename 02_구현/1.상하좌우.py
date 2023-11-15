n = int(input())
moves = input().split()
direction = {"L":(0,-1),
             "R":(0,1),
             "U":(-1,0),
             "D":(1,0)}
start_x,start_y = 0,0
for move in moves:
    mx,my = direction[move]
    if start_x + mx < 0 or start_x + mx >= n or start_y+my < 0 or start_y+my >= n:
        continue
    start_x+=mx
    start_y+=my
print(*[start_x+1,start_y+1])