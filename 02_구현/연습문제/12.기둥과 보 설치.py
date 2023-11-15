n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
answer = list()
def checkTF():
    global answer
    yn = True
    for ans in answer:
        x,y,w = ans
        # 기둥인 경우
        if w == 0:
            if not (y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer):
                yn = False
                break
        # 보 인경우
        else:
            if not ([x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and[x+1,y,1] in answer)):
                yn = False
                break
    return yn
for build in build_frame:
    x,y,w,h = build
    # 삭제인 경우
    if not h :
        if [x,y,w] in answer :
            answer.remove([x,y,w])
        if not checkTF():
            answer.append([x,y,w])

    # 삽입인 경우
    else:
        answer.append([x,y,w])
        if not checkTF():
            answer.remove([x,y,w])
print(sorted(answer))