S = input()
word = list()
num = 0
for s in S:
    # if ord(s) >=65 and ord(s) <= 92 :
    #     word.append(s)
    if s.isalpha():
        word.append(s)
    else:
        num+=int(s)
word.sort()
print(f"{''.join(word)}{num}")
