N = int(input())
X = list(map(int,input().split()))
X.sort()
result = 0
count = 0
for x in X:
    count += 1
    if count >= x:
        result += 1
        count = 0
print(result)