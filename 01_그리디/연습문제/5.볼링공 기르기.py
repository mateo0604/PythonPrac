N,M = map(int,input().split())
balls = list(map(int,input().split()))
result = 0
# 기본 for문
# for i in range(len(balls)-1):
#     for j in range(i+1,len(balls)):
#         if balls[i]!=balls[j]:
#             result+=1

# 수정
arr = [0]*10
for ball in balls:
    arr[ball-1]+=1
for a in arr:
    N-=a
    result+= a * N
print(result)