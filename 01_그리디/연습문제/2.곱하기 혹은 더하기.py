import time
data = list(map(int,list(input())))
start = time.time()
result = 0

# 본인 작성 코드
# for d in data:
#     result = max(result*d, result+d)

# 풀이 코드
for d in data:
    if result <= 1 or d <= 1:
        result += d
    else:
        result *= d

print(result)
print(f"코드 처리 시간 : {time.time() - start}")

