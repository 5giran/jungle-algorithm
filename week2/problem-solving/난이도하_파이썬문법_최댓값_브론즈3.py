# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
# 두마디: index와 value 둘 다 사용해야 할 때는 enumerate() 함수를 사용하자. 리스트 컴프리헨션을 적용해보자.

import sys
input = sys.stdin.readline

n_list = [int(input()) for _ in range(9)]
max_n = max(n_list)
max_i = n_list.index(max_n) + 1
print(f"{max_n}\n{max_i}")
