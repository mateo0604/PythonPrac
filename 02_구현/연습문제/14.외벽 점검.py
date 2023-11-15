from itertools import permutations
def solution(n,weak,dist):
    # 최초 취약갯수
    weak_cnt = len(weak)
    # 원형이므로 취약갯수만큼 +n 추가
    for i in range(weak_cnt):
        weak.append(weak[i]+n)
    # 최소값 1명부터 시작하여 순열을 통해 검사
    for man in range(len(dist)):
        # man 수만큼 순열 추출
        perm = list(permutations(dist,man+1))
        # 검사 시작점 0부터 4 까지  
        for start in range(weak_cnt):
            # 아까 추출한 순열별로 탐색
            for p in perm:
                # 검사에 사용된 순열 개수(번호)
                p_cnt = 1
                # 기준이 된 순열 번호가 탐색할 수 있는 최대 거리
                p_pos = weak[start] + p[p_cnt - 1]
                # 취약점 찾은 개수
                find_cnt = 0
                # 검사 시작점부터 취약개수만큼 검사 시작
                for v in range(start,start+weak_cnt):
                    # 만약 순열 최대거리보다 취약점 거리가 더 멀면 그다음 순열번호 사용
                    if p_pos < weak[v]:
                        p_cnt += 1
                        # 그다음 순열 번호가 순열 길이보다 길면 break 
                        if p_cnt > len(p):
                            break
                        #그 다음 순열번호가 탐색 할 수 있는 최대거리 갱신
                        p_pos = weak[v] + p[p_cnt - 1]
                    # 찾은개수 + 1
                    find_cnt += 1
                # 만약 찾은개수가 취약 개수와 같으면 순열 개수 return    
                if find_cnt == weak_cnt :
                    return p_cnt
    return -1

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
result = solution(n,weak,dist)
print(result)                