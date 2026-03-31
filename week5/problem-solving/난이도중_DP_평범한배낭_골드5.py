# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    dp = [0] * (k+1)
    items = []

    for _ in range(n):
        w, v = map(int, input().split())
        items.append((w, v))

    for w, v in items:
        for i in range(k, w-1, -1):
            dp[i] = max(dp[i], dp[i-w] + v)

    print(dp[k])

if __name__ == "__main__":
    main()