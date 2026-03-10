# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
# 한마디: 

import sys
input = sys.stdin.readline


def hanoi(n, start, to, via):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, via, to)
        print(start, to)
        hanoi(n-1, via, to, start)

n = int(input())
print(2**n - 1) # 하노이의 탑 최소 이동횟수 공식
if n <= 20:
    hanoi(n, 1, 3, 2)