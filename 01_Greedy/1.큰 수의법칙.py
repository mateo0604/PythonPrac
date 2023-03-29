from typing import List

def greedy(n : int, m:int ,k:int,arr : List[int]):
    result = 0
    arr.sort(reverse=True)
    while True:
        for i in range(k):
            if  m == 0:
                break
            result += arr[0]
            m-=1
        if m==0 :
            break
        result += arr[1]
        m-=1
    print(f"결과 : {result}")
    


if __name__ == "__main__":
    n,m,k = map(int,input("숫자 입력 : ").strip().split(" "))
    arr = [int(n) for n in input("배열 입력 : ").strip().split(" ")]
    greedy(n,m,k,arr)