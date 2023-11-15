score = input()
score = list(map(int,list(score)))
ln = len(score) // 2
if sum(score[:ln]) == sum(score[ln:]):
    print("LUCKY")
else:
    print("READY")