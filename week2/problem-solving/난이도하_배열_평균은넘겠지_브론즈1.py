# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
# 한마디: f-string

import sys
input = sys.stdin.readline

c = int(input())
p_list = list()

for _ in range(c):
    data = list(map(int, input().split()))
    count = data[0]
    scores = data[1:]
    avg = sum(scores) / count
    above = sum(1 for s in scores if s > avg)
    
    p_list.append(f"{round(above / count * 100, 3):.3f}%")

for p in p_list:
    print(p)