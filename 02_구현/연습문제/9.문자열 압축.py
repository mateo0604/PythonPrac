def solution(s):
    result = len(s)
    for i in range(1,(len(s)+1)//2 + 1):
        key_cnt = 0
        val_cnt = 0
        word = ''
        prev_val = 1
        for j in range(0,len(s),i):
            if word != s[j:j+i]:
                word = s[j:j+i]
                key_cnt += len(word)
                if prev_val > 1:
                    val_cnt+=len(str(prev_val))
                prev_val = 1
            else:
                prev_val+=1
            print(f"word = {word}, key_cnt = {key_cnt} val_cnt = {val_cnt} prev_val = {prev_val}")
        if prev_val > 1:
            val_cnt += len(str(prev_val))
        print(f"result = {result}, tot = {key_cnt + val_cnt}")
        result = key_cnt+val_cnt if result > key_cnt+val_cnt else result
        
    return result
print(solution('aaaaaaaaaaaabcd'))