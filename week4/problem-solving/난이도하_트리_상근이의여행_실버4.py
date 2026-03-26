# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        for j in range(m):
            a, b = map(int, input().split())
        print(n-1)

if __name__ == "__main__":
    main()