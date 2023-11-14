S = input()
s_dict = {'0':0,'1':0}
key = None
for s in S:
    if not key:
        key = s
    elif key != s:
        s_dict[key] += 1
        key = s
if key:
    s_dict[key] += 1
print(min(s_dict.values()))