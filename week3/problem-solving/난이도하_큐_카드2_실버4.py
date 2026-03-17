# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque

import sys
input = sys.stdin.readline

n = int(input())

card_d = deque([i for i in range(1, n+1, 1)])

while len(card_d) > 1:
    card_d.popleft()
    tem = card_d.popleft()
    card_d.append(tem)

print(card_d[0])