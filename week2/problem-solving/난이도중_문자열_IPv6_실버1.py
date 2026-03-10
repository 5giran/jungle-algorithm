# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
# 두마디: 조건이 여러개면 의사결정 과정을 도식화해보자. 조건의 의존성에 대해 생각하자.

import sys
input = sys.stdin.readline

ip = input.strip().split(":")

if "" in ip:
    emp_idx = ip.idex("")
    ip = [x for x in ip if x != ""]
    cnt = 8 - len(ip)
    ip[emp_idx:emp_idx] = ["0000"] * cnt

for i, v in enumerate(ip):
    if len(v) < 4:
        ip[i] = "0" * (4 - len(v)) + v

result = ":".join(ip)
print(result)