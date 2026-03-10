# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
# 한마디: 자유롭게 구현 후 후에 리스트 컴프리헨션 적용

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    re_cnt, text = input().split()
    r_list = [s * int(re_cnt) for s in text]
    print(''.join(r_list))
