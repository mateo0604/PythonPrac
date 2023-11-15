n = int(input())
## 0~ 59분 59초까지
# 1. 전체 횟수
tot_cnt = 0
# 2. 3이 있는 경우의 수
part_cnt = 0
# 3. 결과 값
result = 0
for i in range(0,60):
    for j in range(0,60):
        tot_cnt += 1
        if "3" in str(i)+str(j):
            part_cnt += 1
for i in range(n+1):
    if "3" in str(i):
        result += tot_cnt
    else:
        result += part_cnt
print(result)