from typing import List

# 일반 while 문
# def greedy(n : int, m:int ,k:int,arr : List[int]):
#     result = 0
#     arr.sort(reverse=True)
#     while True:
#         for i in range(k):
#             if  m == 0:
#                 break
#             result += arr[0]
#             m-=1
#         if m==0 :
#             break
#         result += arr[1]
#         m-=1
#     print(f"결과 : {result}")
    
# 수열 규칙으로 구현
def greedy(n:int,m:int,k:int,arr:List[int]):
    arr.sort(reverse=True)
    first = arr[0]
    second = arr[1]
    result = (m//(k+1))*(first*k + second) + (m%(k+1))*(first)
    print(result)
if __name__ == "__main__":
    n,m,k = map(int,input("숫자 입력 : ").strip().split(" "))
    arr = [int(n) for n in input("배열 입력 : ").strip().split(" ")]
    greedy(n,m,k,arr)