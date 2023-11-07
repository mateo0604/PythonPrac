import sys
n,m = map(int,input().split())
num_list = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
result = max(map(min,num_list))
print(result)