# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
# 한마디: he was like...

import sys
input = sys.stdin.readline

n = int(input()) # 입력값을 int로 변환
n_list = list(map(int, input().split())) # 리스트의 값을 일괄 int로 형변환
prime_cnt = 0

for i in range(n):
    d_list = list()
    num = n_list[i]
    for x in range(1, num + 1):
        if num % x == 0:
            d_list.append(x)
    if len(d_list) == 2: # 약수가 2개만 존재하면(1과 자기 자신) 소수
        prime_cnt += 1

print(prime_cnt)