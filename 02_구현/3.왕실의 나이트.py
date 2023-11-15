n = 8
result = 0
answer = input()
x,y = list(answer)
x = ord(x) - 97
y = int(y)-1
for mx,my in ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)):
    if 0 <= (mx+x) < n and 0 <= (my+y) < n:
        result += 1
print(result)